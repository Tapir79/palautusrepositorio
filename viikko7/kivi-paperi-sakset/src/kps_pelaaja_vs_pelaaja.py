from kivi_paperi_sakset import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):

    def __init__(self):
        super().__init__()

    def tokan_siirto(self):
        return input("Toisen pelaajan siirto: ")
    
    def toisen_pelaajan_eka_valinta(self, _tokan_siirto):
        pass
    
    def siirron_asettaminen(self, _tokan_siirto, _ekan_siirto):
        pass

    
