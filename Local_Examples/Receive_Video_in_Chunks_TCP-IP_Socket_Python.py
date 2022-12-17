import os
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print(f'starting up on {server_address}')
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print(f'connection from {client_address}')

        # Generate a unique filename by appending a number to the end of the filename
        # if the file already exists in the "downloads" folder
        filename = 'received_video.mp4'
        i = 1
        while os.path.exists(os.path.join(os.getcwd(), 'downloads', filename)):
            filename = f'received_video ({i}).mp4'
            i += 1

        # Receive the data in small chunks and write it to a file
        with open(os.path.join(os.getcwd(), 'downloads', filename), 'wb') as f:
            while True:
                data = connection.recv(1024)
                if not data:  # end of file
                    break
                f.write(data)
   
    finally:
        # Clean up the connection
        connection.close()

# This code creates a TCP server that listens for incoming connections on port 10000. When a client connects, the server receives the data in small chunks and writes it to a file named received_video.mp4 in the