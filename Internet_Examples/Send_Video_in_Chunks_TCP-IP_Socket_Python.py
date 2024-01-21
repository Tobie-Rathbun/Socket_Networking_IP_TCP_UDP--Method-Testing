import os
import pickle
import socket
import requests




CHUNK_SIZE = 1024  # chunk the data into 1024-byte pieces

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




def get_public_ip():
    try:
        # Use a service that returns your public IP address
        response = requests.get('https://api64.ipify.org?format=json')
        
        if response.status_code == 200:
            # Parse the JSON response to extract the IP address
            public_ip = response.json()['ip']
            return public_ip
        else:
            print(f"Failed to get public IP. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error getting public IP: {e}")

# Get Public IP Address
PUBLIC_IP = get_public_ip()

if PUBLIC_IP:
    print(f'Public IP Address: {PUBLIC_IP}')
else:
    print('Unable to retrieve public IP address.')



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