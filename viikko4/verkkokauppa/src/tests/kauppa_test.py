import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        # Kaikille testeille yhteiset mockit
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        # Viitegeneraattori palauttaa aina 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # Default asetukset varastolle (voi ylikirjoittaa testeissä)
        self.varasto_mock.saldo.return_value = 10
        self.varasto_mock.hae_tuote.return_value = Tuote(1, "maito", 5)

        # Jokaisessa testissä uusi kauppa
        self.kauppa = Kauppa(
            self.varasto_mock,
            self.pankki_mock,
            self.viitegeneraattori_mock
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_tilisiirtoa_kutsutaan_oikeilla_tiedoilla(self):
        """kutsutaan oikealla asiakkaalla, tilinumeroilla ja summalla"""

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            5
        )