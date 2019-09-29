import unittest
from convert import dcm_to_png
import os


class TestDCM(unittest.TestCase):

    def test_dcm_to_png(self):
        files = os.listdir("/Users/cheese/Src/PythonSrc/dcm-convert/data")
        for file in files:
            if not os.path.isdir(file):
                print("===================")
                print(file)
                print(dcm_to_png("data", file))
