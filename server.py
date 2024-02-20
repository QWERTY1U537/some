import socket
import logging
import json
import random

from  common import addr

logger = logging.getLogger(__name__)
logging.basicConfig()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c = s.bind((addr))
s.listen(5)

s.setblocking(False)
s.settimeout(1)

while True:
    try:
        client_socket = s.accept()
    except TimeoutError:
        continue
    client, (addr, port) = client_socket
    logger.warning(f"{addr} connected from port {port}")

    client.send(str(random.random()).encode)
    # b''.decode()
    # ''.encode
    client.close()
    
    



