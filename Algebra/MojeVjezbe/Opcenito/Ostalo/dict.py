carsList = [
    {
        'make': 'Toyota', 
        'model': 'Prius', 
        'year': 2006, 
        'color': 'gold', 
        'doors': 4,
        'leather': False, 
        'license': 'ABC123', 
        'mileage': 77777
        },
    {
        'make': 'Honda', 
        'model': 'Civic', 
        'year': 2010, 
        'color': 'red', 
        'doors': 2,
        'leather': False, 
        'license': 'DEF444', 
        'mileage': 54321},
    {
        'make': 'Ford', 
        'model': 'Fusion', 
        'year': 2012, 
        'color': 'blue', 
        'doors': 4,
        'leather': True, 
        'license': 'GHI999', 
        'mileage': 24680},
    {
        'make': 'Chevy', 
        'model': 'Volt', 
        'year': 2015, 
        'color': 'black', 
        'doors': 4,
        'leather': False, 
        'license': 'JKL444', 
        'mileage': 7890}
]


def pretraziKorisnike(l: list):
    print("- - pretraga po imenu i prezimenu - -")
    i = input("Ime: ")
    p = input("Prezime: ")
    #koristi se kako bi ispisali poruku ne postoji ili krivi unos
    flag = False 
    for korisnik in l:
        if i.lower() == (korisnik['make']).lower() and p.lower() == (korisnik['model']).lower():
            #ako uđe u petlju, printa model auta i mijenja flag u True te breaka iz for petlje jer smo našli rješenje
            print(korisnik)
            flag = True
            break
    
    #Ovo se ispisuje samo ako nikad nije ušao u gornju if petlju
    if flag == False:
        print("Ne postoji ili krivi unos.")

pretraziKorisnike(carsList)