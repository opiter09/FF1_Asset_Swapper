import os
import sys
import subprocess

if (os.path.exists("model.txt") == False):
    new = open("model.txt", "wt")
    new.write("2")
    new.close()

number = open("model.txt", "rt").read()

subprocess.run(["swap.exe", "e", sys.argv[1], "output", number])