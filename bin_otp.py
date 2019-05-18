#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

with open (sys.argv[1], 'r') as sinput:
    lineNumber = 0
    while lineNumber < int(sys.argv[2]):
        KEY = sinput.readline()
        lineNumber += 1
KEY = KEY[4:]
KEY = KEY.rstrip()

with open (sys.argv[3], 'r') as sinput:
    INPUT = sinput.read()
INPUT = INPUT.rstrip()

Bitstring = ''
for word in INPUT:
    temp = bin(ord(word))[2:]
    while len(temp) < 8:
        temp = '0' + temp
    Bitstring += temp

while len(Bitstring) < 2048:
    Bitstring = '0' + Bitstring

bitIndex = 0
RESULT = ''
while bitIndex < 2048:
    RESULT += bin(int(KEY[bitIndex],2) ^ int(Bitstring[bitIndex],2))[2:]
    bitIndex += 1

Final = ''
temp = ''
for bit in RESULT:
    if len(temp) != 8:
        temp += bit
    else:
        Final += chr(int(temp,2))
        temp = bit
Final += chr(int(temp,2))

print(Final, file=open(sys.argv[4], 'w'))
