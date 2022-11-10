import os
import random
from string import ascii_lowercase as al
import time

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
    QUESTIONS = {}
    QUESTIONS = prepareQuestions(fname_r, QUESTIONS)

    for index, (question, choices) in enumerate(QUESTIONS.items(), start=1):
        ocisti_ekran()
        print(f"\nPitanje {index}:")
        print(f"{question}?")
        choices = choices.copy()
        correct_answer = choices[-1]
        choices.pop(-1)
        random.shuffle(choices)
        labeled_choices = dict(zip(al, (choices)))
        for label, choice in labeled_choices.items():
            print(f"  {label}) {choice}")
        
        while (answer_label := input("\nOdgovor: ")) not in labeled_choices:
            print(f"Molim unesi jedan od {', '.join(labeled_choices)} odgovora.")

        answer = labeled_choices[answer_label]
        if answer == correct_answer:
            print("Točno!")
            time.sleep(2)
        else:
            print(f'''Odgovor je '{correct_answer}', a ne '{answer}' ''')
            time.sleep(2)

def ocisti_ekran():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":

    start(fname_r)
    
    
