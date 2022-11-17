#! /usr/bin/env python3
with open("file.txt") as file:
    lines = file.readlines()
    for line in file:
        print(line.strip().upper())

print(lines)

