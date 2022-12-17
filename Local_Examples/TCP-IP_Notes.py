# Tobie Rathbun 2022

# //// TCP /////
# A TCP (Transmission Control Protocol) server is a network server that listens for incoming connections from clients and sends and receives data over the network using the TCP protocol.

# In a TCP server, the server listens for incoming connections on a specific port
# Ports are numbered from 0 to 65535, and each port can be associated with a specific service or application. For example, port 80 is typically used for HTTP traffic, port 443 is used for HTTPS traffic, and port 22 is used for SSH connections.
# The ports from 0 to 1023 are reserved for well-known services and are typically only used by system processes or by programs executed by privileged users. The ports from 1024 to 49151 are reserved for registered ports and are typically used by common application-level protocols such as HTTP, FTP, and SMTP. The ports from 49152 to 65535 are dynamic and/or private ports that can be used by any application.


# ///// sendall() //////
# In this example, the client connects to the server and sends a message using sendall(). The server receives the message and sends a response back to the client, which is received by the client using the recv() method.
# sendall() can be used to send any type of data over the network, as long as it can be converted to a sequence of bytes. In Python, this means that you can use sendall() to send strings, integers, floating-point numbers, lists, dictionaries, and other data types as long as they can be serialized to a byte sequence.

# To send an image or video over TCP/IP using sendall(), you will need to encode the image or video data into a format that can be transmitted as a sequence of bytes. There are several ways to do this, depending on the type of image or video data you are working with and the requirements of your application.
# One way to encode an image for transmission over TCP/IP is to use a lossless image format such as PNG or GIF. These formats are designed to preserve the quality of the image while minimizing the size of the data. To send an image using these formats, you can use Python's pillow library to load the image, encode it as a byte sequence, and send it using sendall().

# To send a video over TCP/IP, you will need to encode the video data into a format that can be transmitted as a sequence of bytes. One way to do this is to use a video codec such as H.264 or VP9 to compress the video data and wrap it in a container format such as MP4 or MKV. To send a video using this approach, you can use a library such as ffmpeg or gstreamer to encode the video data and send it using sendall().
# Keep in mind that the size of the image or video data you can transmit using sendall() will be limited by the available bandwidth and the memory constraints of your application. It may be necessary to chunk the data into smaller pieces and send them separately in order to transmit large files over the network.


# ///// Over the Internet /////
# To send data over the internet, you will need to use the public IP address of the machine that you want to send the data to, rather than using localhost. The public IP address is the unique address that identifies your machine on the internet, and it can be used by other devices to connect to your machine over the internet.

# To find your IP address in Python using the socket library, you can use the gethostbyname() function, which returns the IP address associated with a given hostname. In this case, you can use the gethostname() function to retrieve the hostname of your machine, and then pass it to the gethostbyname() function to retrieve the corresponding IP address.

import socket

# Get the hostname of the machine
hostname = socket.gethostname()

# Get the IP address associated with the hostname
ip_address = socket.gethostbyname(hostname)

print(f'Your IP address is: {ip_address}')

# This code retrieves the hostname of your machine using the gethostname() function and then uses the gethostbyname() function to retrieve the corresponding IP address. The IP address is then printed to the console.

# Keep in mind that the gethostbyname() function returns the IP address associated with the hostname, which may not necessarily be your public IP address

# A hostname is a human-readable label that is used to identify a device on a network. Hostnames are typically easier to remember and use than IP addresses, which are numerical addresses that are used to identify devices on a network.
# On a home network, hostnames are typically assigned by the router or by the user. For example, you might assign the hostname "my-laptop" to your laptop, or "my-printer" to your printer. On a larger network, such as the internet, hostnames are typically assigned by organizations known as Domain Name System (DNS) providers.
# Hostnames are typically used to identify devices on a network by mapping them to their corresponding IP addresses. For example, when you type "www.example.com" into your web browser, your computer sends a request to a DNS server to resolve the hostname "www.example.com" to its corresponding IP address. The DNS server then returns the IP address to your computer, which uses it to establish a connection to the server at that address.
