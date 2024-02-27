import socket
import json

from  common import addr

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(addr)
data = json.loads(s.recv(500).decode())
print(f'got {data},type {type(data)}')