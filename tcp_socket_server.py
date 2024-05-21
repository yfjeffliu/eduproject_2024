#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

HOST = '0.0.0.0'
PORT = 5001
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')
while True:
    try:
        conn, addr = s.accept()
        print('connected by ' + str(addr))

        indata = conn.recv(1024)
        print('recv: ' + indata.decode())

        outdata = 'echo ' + indata.decode()
        conn.send(outdata.encode())
        

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        conn.close()
    except KeyboardInterrupt:
        s.close()
        print('close')
        break

