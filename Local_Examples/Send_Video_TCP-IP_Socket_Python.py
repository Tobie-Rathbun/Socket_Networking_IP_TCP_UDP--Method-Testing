import socket
import subprocess

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Encode the video as an MP4 file
subprocess.run(['ffmpeg', '-i', 'input.mp4', '-c:v', 'libx264', '-strict', '-2', 'output.mp4'])

# Open the output file and send the data to the server
with open('output.mp4', 'rb') as f:
    data = f.read()
    sock.sendall(data) 