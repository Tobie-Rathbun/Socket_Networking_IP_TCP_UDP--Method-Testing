import socket
from PIL import Image


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Load the image from a file
image = Image.open('image.png')

# Encode the image as a PNG byte sequence
image_bytes = image.tobytes()

# Send the image data to the server
sock.sendall(image_bytes)