import os
import random
import time
from string import ascii_lowercase as al
from datetime import datetime as dt

fname_r = "/config/workspace/Algebra_workspace/Algebra/Vjezbe/quiz/pitanja.txt"
fname_a = "/config/workspace/Algebra_workspace/Algebra/Vjezbe/quiz/score.txt"


def readFile(ime: str):
    exists = os.path.isfile(ime)  # True/False
    if exists:
        try:
            file = open(ime, "r")
            lines = file.readlines()
            file.close()
            return lines
        except:
            print("Dogodila se greška!")
    else:
        print("File ne postoji!")


def appendToFile(s: str, fname: str):
    file = open(fname, "a")
    file.write(s)
    file.close()


if __name__ == "__main__":
    """     s = f"Dino,{int(dt.now().timestamp())},1250\n"
    appendToFile(s, fname_a)
    s = f"ante,{int(dt.now().timestamp())},968\n"
    appendToFile(s, fname_a) """

    lines = readFile(fname_a)
   # print(lines)
    SCORE = {}
    for line in lines:
        elementi = line.strip().split(";")
        SCORE[elementi[0]] = [elementi[1], elementi[2]]
    
    print(SCORE)

