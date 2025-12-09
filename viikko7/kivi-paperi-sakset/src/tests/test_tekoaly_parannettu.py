import pytest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tekoaly_parannettu import TekoalyParannettu


class TestTekoalyParannettu:
    """Tests for the improved AI with memory."""

    def test_alustus(self):
        """Test initialization with memory size."""
        tekoaly = TekoalyParannettu(5)
        siirto = tekoaly.anna_siirto()
        assert siirto in ["k", "p", "s"]

    def test_ensimmainen_siirto_on_kivi(self):
        """Test that first move is always rock."""
        tekoaly = TekoalyParannettu(10)
        siirto = tekoaly.anna_siirto()
        assert siirto == "k"

    def test_toinen_siirto_on_kivi(self):
        """Test that second move is also rock (not enough memory)."""
        tekoaly = TekoalyParannettu(10)
        tekoaly.anna_siirto()
        tekoaly.aseta_siirto("p")
        siirto = tekoaly.anna_siirto()
        assert siirto == "k"

    def test_muistaa_siirrot(self):
        """Test that AI remembers moves."""
        tekoaly = TekoalyParannettu(10)
        tekoaly.anna_siirto()
        
        # Set some moves
        tekoaly.aseta_siirto("k")
        tekoaly.aseta_siirto("k")
        tekoaly.aseta_siirto("p")
        
        # AI should now have pattern to analyze
        siirto = tekoaly.anna_siirto()
        assert siirto in ["k", "p", "s"]

    def test_vastaa_vastustajan_kuvioihin(self):
        """Test that AI responds to opponent patterns."""
        tekoaly = TekoalyParannettu(10)
        tekoaly.anna_siirto()
        
        # Create pattern: opponent plays k -> k -> k
        tekoaly.aseta_siirto("k")
        tekoaly.anna_siirto()
        tekoaly.aseta_siirto("k")
        tekoaly.anna_siirto()
        tekoaly.aseta_siirto("k")
        
        # AI should predict k and play p (paper beats rock)
        siirto = tekoaly.anna_siirto()
        assert siirto == "p"

    def test_muisti_tayttyy(self):
        """Test that memory wraps when full."""
        muistin_koko = 3
        tekoaly = TekoalyParannettu(muistin_koko)
        tekoaly.anna_siirto()
        
        # Fill memory
        for _ in range(muistin_koko + 2):
            tekoaly.aseta_siirto("k")
            tekoaly.anna_siirto()
        
        # Should still work
        siirto = tekoaly.anna_siirto()
        assert siirto in ["k", "p", "s"]

    def test_paperi_voittaa_kiven(self):
        """Test AI plays scissors when paper pattern detected."""
        tekoaly = TekoalyParannettu(10)
        tekoaly.anna_siirto()
        
        # Create pattern: opponent plays p -> p -> p
        tekoaly.aseta_siirto("p")
        tekoaly.anna_siirto()
        tekoaly.aseta_siirto("p")
        tekoaly.anna_siirto()
        tekoaly.aseta_siirto("p")
        
        # AI should predict p and play s (scissors beats paper)
        siirto = tekoaly.anna_siirto()
        assert siirto == "s"

    def test_ei_kaadu_tyhjalla_muistilla(self):
        """Test AI doesn't crash with empty memory."""
        tekoaly = TekoalyParannettu(10)
        siirto = tekoaly.anna_siirto()
        assert siirto == "k"
