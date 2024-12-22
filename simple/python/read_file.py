import os
import sys

if (len(sys.argv) < 2):
    print("Not enough argument, please enter file name as argument.")
    exit()

f = open(sys.argv[1], "r")
print(f.read())
f.close()