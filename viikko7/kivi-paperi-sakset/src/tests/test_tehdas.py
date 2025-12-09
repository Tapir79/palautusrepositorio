import pytest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kivi_paperi_sakset_tehdas import KiviPaperiSaksetTehdas
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class TestKiviPaperiSaksetTehdas:
    """Tests for the game factory class."""

    def test_luo_pelaaja_vs_pelaaja(self):
        """Test creating player vs player game."""
        tehdas = KiviPaperiSaksetTehdas()
        peli = tehdas.luo_peli('a')
        assert peli is not None
        assert isinstance(peli, KPSPelaajaVsPelaaja)

    def test_luo_tekoaly_peli(self):
        """Test creating AI game."""
        tehdas = KiviPaperiSaksetTehdas()
        peli = tehdas.luo_peli('b')
        assert peli is not None
        assert isinstance(peli, KPSTekoaly)

    def test_luo_parempi_tekoaly_peli(self):
        """Test creating improved AI game."""
        tehdas = KiviPaperiSaksetTehdas()
        peli = tehdas.luo_peli('c')
        assert peli is not None
        assert isinstance(peli, KPSParempiTekoaly)

    def test_virheellinen_valinta_palauttaa_none(self):
        """Test invalid choice returns None."""
        tehdas = KiviPaperiSaksetTehdas()
        peli = tehdas.luo_peli('x')
        assert peli is None

    def test_kaikki_pelit_kaynnistyvat(self):
        """Test all game types can be created."""
        tehdas = KiviPaperiSaksetTehdas()
        
        for tyyppi in ['a', 'b', 'c']:
            peli = tehdas.luo_peli(tyyppi)
            assert peli is not None
            assert hasattr(peli, '_tuomari')
            assert hasattr(peli, 'pelaa')
