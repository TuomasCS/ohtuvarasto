

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Tests the functionality of the Varasto class."""

    def setUp(self):
        """Creates a new warehouse before each test."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Tests that a new warehouse starts empty."""
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Tests that a new warehouse has the correct capacity."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Tests that adding products increases the balance."""
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Tests that adding products reduces available space."""
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Tests that removing products returns the correct amount."""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Tests that removing products increases available space."""
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_tilavuus_nollataan(self):
        """Tests that a negative capacity is set to zero."""
        varasto = Varasto(-5)

        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo_nollataan(self):
        """Tests that a negative initial balance is set to zero."""
        varasto = Varasto(10, -3)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_alkusaldo_mahtuu_varastoon(self):
        """Tests that a valid initial balance is accepted."""
        varasto = Varasto(10, 3)

        self.assertAlmostEqual(varasto.saldo, 3)

    def test_liian_suuri_alkusaldo_rajataan_tilavuuteen(self):
        """Tests that an excessive initial balance is limited."""
        varasto = Varasto(10, 15)

        self.assertAlmostEqual(varasto.saldo, 10)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        """Tests that adding a negative amount changes nothing."""
        self.varasto.lisaa_varastoon(5)

        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_liian_suuri_lisays_tayttaa_varaston(self):
        """Tests that an excessive addition fills the warehouse."""
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_ottaminen_palauttaa_nollan(self):
        """Tests that removing a negative amount returns zero."""
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(saatu_maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_liian_suuri_ottaminen_palauttaa_kaiken_ja_tyhjentaa(self):
        """Tests that removing too much empties the warehouse."""
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(8)

        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_palauttaa_oikean_merkkijonon(self):
        """Tests that the string representation is correct."""
        self.varasto.lisaa_varastoon(3)

        self.assertEqual(str(self.varasto), "saldo = 3, vielä tilaa 7")
