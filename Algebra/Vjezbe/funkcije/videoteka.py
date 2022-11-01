"""
Kreirati softver za videoteku. Arhitektura je proizvoljna.

id_naloga

kreirati u formatu npr: 001-ID_KORISNIKA-ID_FILMA-MJESEC-GODINA

001-025-018-11-2022

"""
import time
from datetime import datetime as dt
from prettytable import PrettyTable
import os


baza_korisnika = {

    "korisnici":[
        {
            "id": None,
            "ime": None,
            "vrijeme_kreiranja": None,
            "stanje_racuna": 0
        }
    ],

    "izdani_filmovi": [
        {
            "id_naloga": None,
            "id_kupca": None,
            "id_filma": None,
            "film_vracen": False,
            "vrijeme_kreiranja": None,
            "vrijeme_povrata": None
        }
    ]
}

print(popsi_filmova[0])