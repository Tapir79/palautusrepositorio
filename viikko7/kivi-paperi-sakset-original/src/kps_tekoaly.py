from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):

    def __init__(self, tekoaly= Tekoaly()):
        super().__init__()
        self._tekoaly = tekoaly

    def tokan_siirto(self):
        return self._tekoaly.anna_siirto()
    
    def toisen_pelaajan_eka_valinta(self, tokan_siirto):
        print(f"Tietokone valitsi: {tokan_siirto}")

    def siirron_asettaminen(self, tokan_siirto, _ekan_siirto):
        print(f"Tietokone valitsi: {tokan_siirto}")