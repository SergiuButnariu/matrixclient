#!/usr/bin/env python3

import socket
import numpy as np
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    rec = s.recv(1024)
    data = bytearray(rec)
    counter = 0
    while len(rec) == 1024:
        rec = s.recv(1024)
        data += bytearray(rec)
        counter += 1
    array = np.frombuffer(data)
    np.savetxt('data.csv', array, delimiter=',')
    s.close()
print(len(data))
