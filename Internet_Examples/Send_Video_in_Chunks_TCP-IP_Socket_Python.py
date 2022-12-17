import os
import pickle
import socket

CHUNK_SIZE = 1024  # chunk the data into 1024-byte pieces

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get Public IP Address
PUBLIC_IP = '10.18.18.162'

# Connect the socket to the server
server_address = (PUBLIC_IP, 10000)
print(f'connecting to {server_address}')
sock.connect(server_address)

# Open the video file and read it in chunks
with open(os.path.join(os.getcwd(), 'video.mp4'), 'rb') as f:
    while True:
        chunk = f.read(CHUNK_SIZE)
        if not chunk:  # end of file
            break
        sock.sendall(chunk)

# Close the socket
sock.close()