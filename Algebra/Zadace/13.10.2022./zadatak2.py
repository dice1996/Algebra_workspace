"""
Zadatak 7:
Iz liste ["Jabuka", "Naranca", "Ananas", "Grejp", "Banana", "Jabuka", "Ananas", "Banana"] pronadi i obrisi duplikate
"""

lista = ["Jabuka", "Naranca", "Ananas", "Grejp", "Banana", "Jabuka", "Ananas", "Banana"]
novaLista = []

for item in lista:
    if item not in novaLista:
        novaLista.append(item)
print(f"Lista bez duplikata izgleda ovako: {novaLista}")