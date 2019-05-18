#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
from os import urandom

Index = 1
KeyString = ''
while Index < 501:
    OTP = ''
    while len(OTP) < 2048:
        rand = str(os.urandom(1))
        Bytemap = map(ord, rand)
        setcovert = set(Bytemap)
        shave = ''
        for item in setcovert:
            shave = bin(item)
            shave = shave[2:]
            OTP += shave
    while len(OTP) != 2048:
        OTP = OTP[1:]
    IndexString = str(Index)
    while len(IndexString) < 3:
        IndexString = '0' + IndexString
    KeyString += IndexString + ' ' + OTP + '\n'
    Index += 1
print(KeyString, file=open(sys.argv[1], 'w'))

