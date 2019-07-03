#! /usr/bin/python3

import os
import re

myDict = {}
with open("input.txt", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        # for ch in '~!@#$%^&*()_+"{}[]|?.<>?-':
        #     line = line.replace(ch,"")
        for word in line.split():
            if not word.isalpha():
                continue
            if len(word) < 2:
                continue
            lWord = word.lower()
            if lWord in myDict:
                myDict[lWord] += 1
            else:
                myDict[lWord] = 1

items = list(myDict.items())
items.sort(key=lambda x:x[1],reverse=True)

with open("output.txt", 'w', encoding="utf-8") as f:
    for key, value in items:
        f.write(f"{key}, {value} \n")
