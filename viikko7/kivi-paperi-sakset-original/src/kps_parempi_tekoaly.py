from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):

    def __init__(self, tekoaly= TekoalyParannettu(10)):
        super().__init__()
        self._tekoaly = tekoaly

    def tokan_siirto(self):
        return self._tekoaly.anna_siirto()
    
    def toisen_pelaajan_eka_valinta(self, tokan_siirto):
        print(f"Tietokone valitsi: {tokan_siirto}")

    def siirron_asettaminen(self, tokan_siirto, ekan_siirto):
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(ekan_siirto)