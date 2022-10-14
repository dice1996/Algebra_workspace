"""
Zadatak 9:
['x', 'y']
n = 5
rezultat mora biti: ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5']
"""

lista = ["x","y"]
n = 5
rezultat = []

for i in range(n):
    for j in range(len(lista)):
        rezultat.append(lista[j] + str(i+1))
print(rezultat)