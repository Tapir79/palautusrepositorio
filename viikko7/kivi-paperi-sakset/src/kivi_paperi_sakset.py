from tuomari import Tuomari

class KiviPaperiSakset:
    def __init__(self, tuomari=Tuomari()):
        self._tuomari = tuomari
        
    def pelaa(self):
        ekan_siirto, tokan_siirto = self.tee_siirrot()
        self.toisen_pelaajan_eka_valinta(tokan_siirto)
        
        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.pelikierros()
        
        print("Kiitos!")
        print(self._tuomari)

    
    def pelikierros(self):
        self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
        print(self._tuomari)

        ekan_siirto, tokan_siirto = self.tee_siirrot()

        self.siirron_asettaminen(tokan_siirto, ekan_siirto)


    def tee_siirrot(self):
        ekan_siirto = self.ekan_siirto()
        tokan_siirto = self.tokan_siirto()

        return ekan_siirto, tokan_siirto


    def ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def tokan_siirto(self):
        raise IndexError("Tämä metodi pitää korvata aliluokassa")
    
    def toisen_pelaajan_eka_valinta(self, tokan_siirto):
        raise IndexError("Tämä metodi pitää korvata aliluokassa")

    def siirron_asettaminen(self, tokan_siirto, ekan_siirto):
        raise IndexError("Tämä metodi pitää korvata aliluokassa")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"