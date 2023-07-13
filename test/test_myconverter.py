import os
import unittest
from myconverter.converter import MyConverter


'''
This is a simple unittest for MyConverter class, which can convert png, heic, tiff, pdf to png.

Now, let's convert assertequal part to compare with True

self.assertEqual(  
    cvt.convert_png2png(),
    True,
)

'''
TEST_RESULT_FOLDER = os.path.join("test", "test_results")


class Test(unittest.TestCase):
    def test_convert_png2png(self):
        """Test convert png to png"""
        cvt = MyConverter(
            input_file_path=os.path.join("test", "testcases", "test.png"),
            output_file_path=os.path.join("test", "test_results", "out_test_png.png"),
        )
        self.assertEqual(
            cvt.convert(),
            True,
        )

    def test_convert_heic2png(self):
        """Test convert heic to png"""
        cvt = MyConverter(
            input_file_path=os.path.join("test", "testcases", "test.heic"),
            output_file_path=os.path.join("test", "test_results", "out_test_heic.png"),
        )
        self.assertEqual(
            cvt.convert(),
            True,
        )

    def test_convert_tiff2png(self):
        """Test convert tiff to png"""
        cvt = MyConverter(
            input_file_path=os.path.join("test", "testcases", "test.tiff"),
            output_file_path=os.path.join("test", "test_results", "out_test_tiff.png"),
        )
        self.assertEqual(
            cvt.convert(),
            True,
        )

    def test_convert_pdf2png(self):
        """Test convert pdf to png"""
        cvt = MyConverter(
            input_file_path=os.path.join("test", "testcases", "test.pdf"),
            output_file_path=os.path.join("test", "test_results", "out_test_pdf.png"),
        )
        self.assertEqual(
            cvt.convert(),
            True,
        )
    def check_convert_file(self):
        """Check whether there is a  file converted is in test_results folder"""
        for file in os.listdir(TEST_RESULT_FOLDER):
            if file.endswith(".png"):
                return True
        return False
    
if __name__ == "__main__":
    # check if folder test_reults not exists, create it
    if not os.path.exists(TEST_RESULT_FOLDER):
        os.mkdir(TEST_RESULT_FOLDER)
    # run unittest
    unittest.main()
