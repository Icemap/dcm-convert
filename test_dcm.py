import unittest
from convert import dcm_to_png


class TestDCM(unittest.TestCase):

    def test_dcm_to_png(self):
        print(dcm_to_png("data", "00D0C551.dcm"))
