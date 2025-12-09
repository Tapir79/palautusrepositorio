import pytest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tuomari import Tuomari


class TestTuomari:
    """Tests for the Tuomari (Referee) class."""

    def test_tuomari_alkutilanne(self):
        """Test initial state of the referee."""
        tuomari = Tuomari()
        assert tuomari.ekan_pisteet == 0
        assert tuomari.tokan_pisteet == 0
        assert tuomari.tasapelit == 0

    def test_tasapeli(self):
        """Test tie scenario."""
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("k", "k")
        assert tuomari.ekan_pisteet == 0
        assert tuomari.tokan_pisteet == 0
        assert tuomari.tasapelit == 1

    def test_eka_voittaa_kivi_voittaa_sakset(self):
        """Test first player wins with rock vs scissors."""
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("k", "s")
        assert tuomari.ekan_pisteet == 1
        assert tuomari.tokan_pisteet == 0
        assert tuomari.tasapelit == 0

    def test_eka_voittaa_paperi_voittaa_kiven(self):
        """Test first player wins with paper vs rock."""
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("p", "k")
        assert tuomari.ekan_pisteet == 1
        assert tuomari.tokan_pisteet == 0

    def test_eka_voittaa_sakset_voittaa_paperin(self):
        """Test first player wins with scissors vs paper."""
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("s", "p")
        assert tuomari.ekan_pisteet == 1
        assert tuomari.tokan_pisteet == 0

    def test_toka_voittaa(self):
        """Test second player wins."""
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("k", "p")
        assert tuomari.ekan_pisteet == 0
        assert tuomari.tokan_pisteet == 1
        assert tuomari.tasapelit == 0

    def test_usea_kierros(self):
        """Test multiple rounds."""
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("k", "s")  # eka voittaa
        tuomari.kirjaa_siirto("p", "k")  # eka voittaa
        tuomari.kirjaa_siirto("s", "k")  # toka voittaa
        tuomari.kirjaa_siirto("p", "p")  # tasapeli
        
        assert tuomari.ekan_pisteet == 2
        assert tuomari.tokan_pisteet == 1
        assert tuomari.tasapelit == 1

    def test_str_method(self):
        """Test string representation."""
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("k", "s")
        tuomari.kirjaa_siirto("p", "p")
        
        result = str(tuomari)
        assert "Pelitilanne: 1 - 0" in result
        assert "Tasapelit: 1" in result
