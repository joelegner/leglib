from leglib.structural import BuildingCode
from leglib.structural import FBC2010
from leglib.structural import IBC2009
from leglib.structural import NONE
from leglib.structural import codes
import leglib.structural.asce7_10 as asce7
import unittest


class TestBuildingCode(unittest.TestCase):

    def test_name(self):
        from leglib.structural import FBC2010
        self.assertEqual("%s" % FBC2010, "2010 FBC")

    def test_default_codes(self):
        self.assertEqual(IBC2009.asce7.__name__, "leglib.structural.asce7_05")
        self.assertEqual(FBC2010.asce7.__name__, "leglib.structural.asce7_10")
        self.assertEqual(NONE.asce7.__name__, "leglib.structural.asce7_05")
        self.assertEqual(str(FBC2010), "2010 FBC")
        self.assertEqual(str(IBC2009), "2009 IBC")
        self.assertTrue(FBC2010 in codes)
        self.assertTrue(IBC2009 in codes)
        self.assertTrue(NONE in codes)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
