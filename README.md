Vibe: Real-Time Audio Broadcast System
Project Overview
Vibe is a full-stack, real-time audio broadcasting system designed to solve the common problem of synchronized media consumption in multi-user environments. This application allows a single host computer to capture its system audio and stream it to multiple clients simultaneously, enabling a shared listening experience without disturbing others.

The project was conceived to address the challenge of group movie nights or music sessions in shared living spaces like college hostels, where connecting multiple devices for synchronized audio is typically not possible.

Technical Highlights
Client-Server Architecture: Developed a classic client-server model with a Python back-end and a web-based front-end.

Real-Time Data Streaming: Utilized the WebSocket protocol for a persistent, bi-directional connection to stream audio data from the server to all connected clients with low latency.

Asynchronous Programming: Implemented Python's asyncio library to handle multiple client connections concurrently, ensuring a smooth and responsive experience for all users.

System-Level Audio Capture: Overcame complex, platform-specific audio driver issues on Windows by integrating a virtual audio device and the pyaudio library to reliably capture system audio for streaming.

Technologies Used
Back-End: Python 3.x, pyaudio, websockets, numpy, asyncio

Front-End: HTML5, CSS3, JavaScript (Web Audio API)

Tools: Git, GitHub, VS Code, VB-CABLE Virtual Audio Device

Setup and Usage
Clone the repository:

git clone [https://github.com/](https://github.com/)[Your_Username]/Vibe-Audio-Stream.git
cd Vibe-Audio-Stream

Install dependencies:

pip install pyaudio websockets numpy

Install Virtual Audio Cable (Windows):

Download and install the VB-CABLE Virtual Audio Device from their official website.

In your Windows sound settings, set the "CABLE Input" as your default playback device.

Run the server:

In your terminal, run the Python server script. The script will automatically detect the virtual cable device.

python server.py

Connect a client:

Open the audio_client.html file in a modern web browser.

Click the "Connect" button. The web client will receive and play the audio from the host computer.

Lessons Learned & Future Improvements
This project was a deep dive into real-world debugging, particularly in the realm of system-level audio. Initial challenges with hardcoded device IDs and unsupported blocking stream APIs highlighted the importance of robust error handling and platform-specific solutions.

Future improvements could include adding a GUI for the server, implementing different audio codecs for better compression, and building a user interface for selecting the audio device directly from the client.
