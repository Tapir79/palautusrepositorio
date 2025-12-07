from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class KiviPaperiSaksetTehdas():
    """Pelitehdasluokka, joka osaa luoda eri pelejä."""

    def __init__(self):
        self._pelit = {
            'a': KPSPelaajaVsPelaaja,
            'b': KPSTekoaly,
            'c': KPSParempiTekoaly
        }

    def luo_peli(self, tyyppi):
        if tyyppi in self._pelit:
            return self._pelit[tyyppi]() 
        return None