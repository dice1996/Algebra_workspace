from random import randint

number = int()
play = 1
win = 0
lives = 0

def start_game(lives, win):
    while lives > 0 and win != 1:
        print(f"\nPreostalo {lives} života")
        guess = input("Unesi broj: ")
        win = check_guess(int(number), int(guess))
        if win != 1:
            lives = deduct_lives(lives)
        if lives == 0:
            print("\nNemaš više života!\n")
            return
        if win == 1:
            print("Pogodio si broj!\n")
        elif win == -1:
            print("Gađaj na više!\n")
        elif win == 0:
            print("Gađaj na niže!\n")


def deduct_lives(lives):
    return lives - 1


def rand_number():
    return randint(1, 100)


def check_guess(number, guess):
    if guess == number:
        win = 1
    elif guess < number:
        win = -1
    elif guess > number:
        win = 0
    return win


def det_lives(input):
    if input == 'l':
        return 10
    else:
        return 5


while play:
    number = rand_number()
    print(
        "\nDobrodošao U Igru GuessTheNumber\nPravila igre su jednostavna, sve što moraš jest pogoditi na koji broj između 1 i 100 upravo mislim. Lako, zar ne?"
    )
    while True:
        lives = input("Želiš li laku ili tešku igru. Unesi 'l' ili 't' sada: ")
        if lives == "l" or lives == "t":
            lives = det_lives(lives)
            break
        else:
            print("Ponovi unos!")
    #print(f"\nCheat: traženi broj je {number}\n")
    print("Igra upravo počinje!\n")
    start_game(lives, win)
    play = 0
print("Igra završena!")