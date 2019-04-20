#!/usr/bin/python

file = open("aoliver.csv","w")

read_file = open("./data/aoliver_20190418120000_1.csv","r")

for line in read_file.readlines():
    file.write(line)
