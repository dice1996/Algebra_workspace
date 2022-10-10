"""
Write a program to count the occurence of even number and odd number between the range
"""

prviBroj = int(input("Unesi prvi broj raspona: "))
drugiBroj = int(input("Unesi drugi broj raspona: "))

if drugiBroj < prviBroj:
    print("\nDrugi broj ne smije biti manji od prvog broja! Radim zamjenu varijabli...\n")
    pomocna = prviBroj
    prviBroj = drugiBroj
    drugiBroj = pomocna
    print("Zamjena napravljena. Nastavljam program....\n")

even = 0
odd = 0

for broj in range(prviBroj, drugiBroj+1):
    if broj%2 == 0:
        even += 1
    else:
        odd += 1

print(f"\nBroj parnih brojeva je {even}\nBroj neparnih brojeva je {odd}\nRaspon brojeva je ({prviBroj}, {drugiBroj})")