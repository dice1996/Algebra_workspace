import os

fname = "/config/workspace/Algebra_workspace/Algebra/Vjezbe/quiz/pitanja.txt" 

def readFile(ime: str):
    exists = os.path.isfile(ime)    
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

linije = readFile(fname)

for linija in linije:
    elementi = linija.strip().split(";")
    print(elementi)