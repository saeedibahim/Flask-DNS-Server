# get_ip.py
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"Your local IP is: {local_ip}")