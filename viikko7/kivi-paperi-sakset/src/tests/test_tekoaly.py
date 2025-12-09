import pytest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tekoaly import Tekoaly


class TestTekoaly:
    """Tests for the basic AI class."""

    def test_tekoaly_palauttaa_siirron(self):
        """Test that AI returns valid moves."""
        tekoaly = Tekoaly()
        siirto = tekoaly.anna_siirto()
        assert siirto in ["k", "p", "s"]

    def test_tekoaly_muuttaa_siirtoa(self):
        """Test that AI cycles through moves."""
        tekoaly = Tekoaly()
        
        # First three moves should cycle k -> p -> s
        siirto1 = tekoaly.anna_siirto()
        siirto2 = tekoaly.anna_siirto()
        siirto3 = tekoaly.anna_siirto()
        
        assert siirto1 == "p"
        assert siirto2 == "s"
        assert siirto3 == "k"

    def test_tekoaly_kierto_jatkuu(self):
        """Test that AI continues cycling."""
        tekoaly = Tekoaly()
        
        for _ in range(3):
            tekoaly.anna_siirto()
        
        # After full cycle, should start again
        siirto = tekoaly.anna_siirto()
        assert siirto == "p"

    def test_aseta_siirto_ei_tee_mitaan(self):
        """Test that aseta_siirto doesn't affect basic AI."""
        tekoaly = Tekoaly()
        siirto1 = tekoaly.anna_siirto()
        
        tekoaly.aseta_siirto("k")
        
        siirto2 = tekoaly.anna_siirto()
        # Should continue normal cycle
        assert siirto2 == "s"
