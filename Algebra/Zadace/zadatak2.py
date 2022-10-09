"""
2. zadatak

unos broja - dokazati da li je broj integer ili float
 
"""

broj = input("Unesi broj za provjeru: ")

try:
    broj = int(broj)
    print(f"Uneseni broj {broj} je {type(broj)}")
except ValueError:
    try:
        broj = float(broj)
        print(f"Uneseni broj {broj} je {type(broj)}")
    except ValueError:
        print("Unos nije broj!")