import asyncio
import websockets
import sounddevice as sd
import numpy as np

connected_clients = set()


def get_virtual_cable_device_id():
    devices = sd.query_devices()
    for idx, device in enumerate(devices):
        if "VB-Audio Virtual" in device['name'] and device['max_input_channels'] > 0:
            print(f"Found VB-Audio Virtual Cable input device: ID={idx}, Name={device['name']}")
            return idx
    return None


async def handler(websocket):
    print(f"Client connected: {websocket.remote_address}")
    connected_clients.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        print(f"Client disconnected: {websocket.remote_address}")
        connected_clients.remove(websocket)


async def audio_stream():
    samplerate = 44100
    blocksize = 1024
    channels = 2

    device_id = get_virtual_cable_device_id()
    if device_id is None:
        print("VB-Audio Virtual Cable not found as input device. Ensure it is enabled and set as default.")
        return

    print(f"Using VB-Audio Virtual Cable device ID: {device_id}")

    try:
        # Open InputStream with explicit format
        stream = sd.InputStream(device=device_id,
                                samplerate=samplerate,
                                channels=channels,
                                dtype='int16',
                                blocksize=blocksize)
    except sd.PortAudioError as e:
        print(f"Error opening audio stream: {e}")
        return

    async with websockets.serve(handler, "localhost", 8080):
        print("WebSocket server started on ws://localhost:8080")
        with stream:
            print("Audio streaming started from VB-Audio Virtual Cable.")
            while True:
                audio_data, overflowed = stream.read(blocksize)
                if overflowed:
                    print("Warning: Audio buffer overflow occurred!")
                if connected_clients:
                    audio_data_bytes = audio_data.tobytes()
                    print(f"Sending audio chunk size: {len(audio_data_bytes)} bytes")
                    tasks = [asyncio.create_task(client.send(audio_data_bytes)) for client in connected_clients]
                    await asyncio.gather(*tasks)
                await asyncio.sleep(0.01)


async def main():
    await audio_stream()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer stopped.")
