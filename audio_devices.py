import sounddevice as sd

def list_audio_devices():
    """
    Lists all available audio devices and their properties.
    """
    print("Listing all audio devices:")
    print("--------------------------------------------------")
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        print(f"Device ID: {i}")
        print(f"  Name: {device['name']}")
        print(f"  Max Input Channels: {device['max_input_channels']}")
        print(f"  Max Output Channels: {device['max_output_channels']}")
        print("--------------------------------------------------")

if __name__ == "__main__":
    list_audio_devices()
