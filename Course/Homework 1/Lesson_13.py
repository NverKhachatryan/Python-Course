from random import random


def makeFile(filename):
    f = open(filename, 'w')
    f.close()
    for i in range(0, 4000000000):
        f = open(filename, 'a')
        f.write(str(int(random() * 200)) + '\n')
        f.close()

print(makeFile('test.txt'))

def sortFile(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    lines.sort()
    f = open('sorted.txt', 'w')
    for line in lines:
        f.write(line)
    f.close()