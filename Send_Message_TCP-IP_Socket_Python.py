import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('localhost', 10000)
print(f'connecting to {server_address}')
sock.connect(server_address)

try:
    # Send a message to the server
    message = 'Hello, server!'
    sock.sendall(message.encode())

    # Receive the response from the server
    response = sock.recv(1024).decode()
    print(f'received response: {response}')
finally:
    # Clean up the connection
    sock.close()
