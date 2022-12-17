import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
server_address = ('localhost', 10000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    try:
        # Receive data in 1024-byte chunks
        while True:
            data = connection.recv(1024)
            if data:
                # Send data back to the client
                connection.sendall(data)
            else:
                # No more data, close the connection
                break
    finally:
        # Clean up the connection
        connection.close()
