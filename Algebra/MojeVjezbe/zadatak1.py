""""
Input: 6

Expected Output
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""

try:
    broj = int(input("Unesi broj ponavljanja: "))
except:
    print("Nije unesen cijeli broj. Ovdje program završava!")
counter = 0
for i in range(1, broj+1):
    counter +=1
    for j in range(0, counter):
        print(f"{counter}", end=" ")
    print("")