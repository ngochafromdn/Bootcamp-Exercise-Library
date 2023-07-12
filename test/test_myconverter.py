import unittest
from myconverter.converter import MyConverter
import os


class Test(unittest.TestCase):
    def test_convert_png2png(self):
        cvt = MyConverter(input_file_path="/testcases/test.png", output_file_path="test_results/out_test_png.png")
        self.assertEqual(cvt.convert(), "Success. File is saved in test_results/out_test_png.png")
    
    def test_convert_heic2png(self):
        cvt = MyConverter(input_file_path="/testcases/test.heic", output_file_path="test_results/out_test_heic.png")
        self.assertEqual(cvt.convert(), "Success. File is saved in test_results/out_test_heic.png")
    
    def test_convert_tiff2png(self):
        cvt = MyConverter(input_file_path="/testcases/test.tiff", output_file_path="test_results/out_test_tiff.png")
        self.assertEqual(cvt.convert(), "Success. File is saved in test_results/out_test_tiff.png")
    
    def test_convert_pdf2png(self):
        cvt = MyConverter(input_file_path="/testcases/test.pdf", output_file_path="test_results/out_test_pdf.png")
        self.assertEqual(cvt.convert(), "Success. File is saved in test_results/out_test_pdf.png")

if __name__ == "__main__":
    # check if folder test_reults not exists, create it
    if not os.path.exists("test_results"):
        os.mkdir("test_results")
    # run unittest
    unittest.main()