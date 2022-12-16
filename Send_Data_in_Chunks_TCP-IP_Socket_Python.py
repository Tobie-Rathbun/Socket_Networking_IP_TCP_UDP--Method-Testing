import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

CHUNK_SIZE = 1024  # chunk the data into 1024-byte pieces

# Open the file and read it in chunks
with open('large_file.dat', 'rb') as f:
    while True:
        chunk = f.read(CHUNK_SIZE)
        if not chunk:  # end of file
            break
        sock.sendall(chunk)
        
# In this example, the data is read in chunks of 1024 bytes and sent to the server using sendall(). This allows you to transmit large files over the network without having to load the entire file into memory at once.
# You can also use this approach to send data of any type, not just files. For example, you can use a loop to chunk a large list or dictionary into smaller pieces and send them separately using sendall()

import pickle
CHUNK_SIZE = 1024  # chunk the data into 1024-element pieces

# Split the data into chunks
data = [1, 2, 3, 4, 5, ...]  # large list of data
for i in range(0, len(data), CHUNK_SIZE):
    chunk = data[i:i + CHUNK_SIZE]
    sock.sendall(pickle.dumps(chunk))
    
# This approach can be useful when transmitting large amounts of data over the network, as it allows you to send the data in smaller pieces that are more manageable and easier to transmit.
