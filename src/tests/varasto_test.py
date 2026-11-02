import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    def test_negatiivinen_tilavuus_nollataan(self):
        v = Varasto(-100.0)
        self.assertAlmostEqual(v.tilavuus, 0)

    def test_negatiivinen_alkusaldo_nollataan(self):
        v = Varasto(100.0, -50.7)
        self.assertAlmostEqual(v.saldo, 0)

    def test_alkusaldo_mahtuu_varastoon(self):
        v = Varasto(100.0, 20.0)
        self.assertAlmostEqual(v.saldo, 20.0)

    def test_liian_suuri_alkusaldo_rajataan_tilavuuteen(self):
        v = Varasto(100.0, 150.0)
        self.assertAlmostEqual(v.saldo, 100.0)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(3)
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 3)

    def test_liian_suuri_lisays_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(1000)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_otto_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(saatu_maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_liian_suuri_otto_palauttaa_koko_saldon(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(1000)

        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_palauttaa_saldon_ja_tilan(self):
        self.varasto.lisaa_varastoon(4)

        self.assertEqual(str(self.varasto), "saldo = 4, vielä tilaa 6")
