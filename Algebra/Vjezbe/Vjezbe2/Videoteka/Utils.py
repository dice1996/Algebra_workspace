import os

class Utils:

    @staticmethod
    def ispisiIzbornik(izbornik: dict):
        for opcija in izbornik.keys():
            print(f"{opcija}:\t{izbornik[opcija]}")
            
        print("_" * 30) 

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def unosOpcije(izbornik):
        while True:
            print("GLAVNI IZBORNIK\n")
            Utils.ispisiIzbornik(izbornik)
            izbor = Utils.unesiCijeliBroj("\nUnesi opciju iz gornjeg izbornika: ")
            if izbor not in izbornik.keys():
                print("Unije validan unos! Pokusaj ponovno!")
                time.sleep(2)
                clear_screen()
            else:
                if izbor == 0:
                    Utils.clear_screen()
                    #print("Kraj programa!")
                    return 0
                else:
                    return izbor

    @staticmethod
    def unesiCijeliBroj(text = None, index = None):
        while True:
            try:
                if text is None and index is None:
                    return int(input("Unesi broj: "))
                elif text is None and index is not None:
                    return int(input(f"Unesi {index}. broj: "))
                else:
                    return int(input(text))
            except:
                print("Krivi unos")