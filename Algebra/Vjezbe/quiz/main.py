import os
import random
from string import ascii_lowercase as al
import time
import math
from datetime import datetime as dt

fname_r = "/config/workspace/Algebra_workspace/Algebra/Vjezbe/quiz/pitanja.txt" 
fname_a = "/config/workspace/Algebra_workspace/Algebra/Vjezbe/quiz/score.txt"

def readFile(ime: str):
    exists = os.path.isfile(ime)   #True/False 
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

def appendToFile(s : str, fname: str):
    file = open(fname, "a")
    file.write(s)
    file.close()

def prepareQuestions(fname_r,  QUESTIONS: dict):

    linije = readFile(fname_r)
    for linija in linije:
        elementi = linija.strip().split(";")
        elementi.pop(0)
        QUESTIONS[elementi[0]] = [elementi[1], elementi[2], elementi[3], elementi[4], elementi[5]]
    
    l = list(QUESTIONS.items())
    random.shuffle(l)
    QUESTIONS = dict(l)
    return QUESTIONS

def start(fname_r):
    ocisti_ekran()
    QUESTIONS = {}
    QUESTIONS = prepareQuestions(fname_r, QUESTIONS)
    points = 0
    for index, (question, choices) in enumerate(QUESTIONS.items(), start=1):
        ocisti_ekran()
        print(f"\nPitanje {index}:")
        print(f"{question}\n")
        choices = choices.copy()
        correct_answer = choices[-1]
        choices.pop(-1)
        random.shuffle(choices)
        labeled_choices = dict(zip(al, (choices)))
        for label, choice in labeled_choices.items():
            print(f"  {label}) {choice}")
        
        start_time = time.time()
        while (answer_label := input("\nOdgovor: ")) not in labeled_choices:
            print(f"Molim unesi jedan od {', '.join(labeled_choices)} odgovora.")
        end_time = time.time()

        time_s = (end_time - start_time)

        answer = labeled_choices[answer_label]
        if answer == correct_answer:
            print("Točno!")
            points = points + (1000 - (1000*(time_s*1000))/(1000 + (time_s*1000))) #formula je: points + (A - Ax/(A-x))
            time.sleep(2)
        else:
            print(f'''Odgovor je '{correct_answer}', a ne '{answer}' ''')
            points = points - (1000 - (1000*(time_s*1000))/(1000 + (time_s*1000)))#formula je: points - (A - Ax/(A-x))
            if points < 0:
                points = 0
            time.sleep(2)
    return points

def ocisti_ekran():
    os.system("cls" if os.name == "nt" else "clear")

def ispisi_rezultat(fname_a):
    lines = readFile(fname_a)
   # print(lines)
    SCORE = {}
    for line in lines:
        elementi = line.strip().split(";")
        SCORE[elementi[0]] = [elementi[1], elementi[2]]
    ime = None
    rez = 0
    for item in SCORE.items():
        ime = item[0]
        rez = item[1][0]

        if rez < item[1][0]:
            ime = item[0]
            rez = item[1][0]
    return [ime, rez]

def highScore(fname_a):
    ocisti_ekran()
    high_score = ispisi_rezultat(fname_a)
    print(f"Poslijednji najbolji rezultat ima igrac {high_score[0]} s brojem bodova: {high_score[1]}!\nSretno!")
    time.sleep(4)
    ocisti_ekran()
    return high_score


if __name__ == "__main__":
    high_score = highScore(fname_a)
    name = input("Unesi ime igraca: ")
    points = start(fname_r)
    rezultat = f"{name};{round(points, 2)};{int(dt.now().timestamp())}\n"
    appendToFile(rezultat, fname_a)
    ocisti_ekran()
    if float(points) > float(high_score[1]):
        print(f"Tvoj broj bodova je {int(points)} i trenutno najbolji rezultat!\nBravo!")
    else:
        print(f"Tvoj broj bodova je {int(points)}!\nBravo!")