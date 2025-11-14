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

        # Viitegeneraattori palauttaa aina saman viitteen
        self.viitegeneraattori_mock.uusi.return_value = 42

        # Määritellään varaston käyttäytyminen id:n mukaan
        def saldo_side_effect(tuote_id):
            # Molempia tuotteita on varastossa
            if tuote_id in [1, 2]:
                return 10
            return 0  # kaikki muut tuotteet loppu

        def hae_tuote_side_effect(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 3)
            if tuote_id == 3:
                return Tuote(3, "wagyu", 4000)
            return None  # tuntematon tuote

        self.varasto_mock.saldo.side_effect = saldo_side_effect
        self.varasto_mock.hae_tuote.side_effect = hae_tuote_side_effect

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

    def test_kahden_eri_tuotteen_osto_onnistuu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            8
        )

    def test_kahden_saman_tuotteen_osto_onnistuu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            10
        )

    def test_kahden_eri_tuotteen_ostoa_yritetaan_vaikka_toinen_on_loppu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            5
        )


    def test_aloita_asiointi_nollaa_edellisen_ostoksen(self):
        # ensimmäinen ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)    # maito 5 €
        self.kauppa.tilimaksu("pekka", "1111")

        # varmista että summa oli 5 €
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "1111",
            "33333-44455",
            5
        )

        # toinen ostos alkaa
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)    # leipä 3 €
        self.kauppa.tilimaksu("matti", "2222")

        # varmista että edellisen ostoksen hinta EI tule mukaan
        self.pankki_mock.tilisiirto.assert_called_with(
            "matti",
            42,
            "2222",
            "33333-44455",
            3
        )

    def test_kauppa_pyytää_uuden_viitenumeron_jokaiseen_maksuun(self):
        # ensimmäinen ostotapahtuma
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "1111")

        # viitteen pitäisi olla pyydetty kerran
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        # toinen ostotapahtuma
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("matti", "2222")

        # nyt pyydetty kaksi kertaa
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        # kolmas ostotapahtuma
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("liisa", "3333")

        # nyt kolme kertaa
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)

   