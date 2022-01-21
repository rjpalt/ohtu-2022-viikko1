import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):

    def test_konstruktori_virheellinen_saldo_nollataan(self):
        vararasto = Varasto (10, -5)
        self.assertAlmostEqual(vararasto.saldo, 0)
        ## Pitää olla 0



    def test_lisaa_varastoon_yli(self):

        vararasto = Varasto(10, 5)
        vararasto.lisaa_varastoon(200)
        self.assertEqual(vararasto.saldo, 10)



    def setUp(self):
        self.varasto = Varasto(10)

    def test_lisaa_varastoon_virhe(self):

        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)


    def test_ota_varastosta_nolla(self):

        palaute = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(palaute, 0.0)


    def test_anna_kaikki_varastosta(self):

        self.varasto.lisaa_varastoon(10)
        palautus = self.varasto.ota_varastosta(15)

        self.assertAlmostEqual(palautus, 10)


    def test_tekstin_palautus(self):

        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")


    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_saldo_nolla_negalla(self):
        varasto = Varasto(-1)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

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
