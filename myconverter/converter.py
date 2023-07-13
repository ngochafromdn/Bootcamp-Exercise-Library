import os
import shutil
import pyheif
import fitz
from PIL import Image
import logging


class MyConverter:
    def __init__(self, input_file_path: str, output_file_path: str) -> None:
        """
        Initialize MyConverter class
        Parameters:
            input_file_path (str): input file path
            output_file_path (str): output file path
        """
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.ext = self.extension_file()

    def extension_file(self) -> str:
        """Get file extension"""
        return os.path.splitext(self.input_file_path)[1]

    def convert_png2png(self) -> str:
        """Convert png to png"""
        shutil.copyfile(self.input_file_path, self.output_file_path)
        logging.info(f"Success. File is saved in {self.output_file_path}")
        return True

    def convert_heic2png(self) -> str:
        """Convert heic to png"""
        heic_img = pyheif.read(self.input_file_path)
        image = Image.frombytes(
            heic_img.mode,
            heic_img.size,
            heic_img.data,
            "raw",
            heic_img.mode,
            heic_img.stride,
        )
        image.save(self.output_file_path)

        logging.info(f"Success. File is saved in {self.output_file_path}")
        return True

    def convert_tiff2png(self) -> str:
        """Convert tiff to png"""
        im = Image.open(self.input_file_path)
        im.thumbnail(im.size)
        im.save(self.output_file_path, "png", quality=100)

        logging.info(f"Success. File is saved in {self.output_file_path}")
        return True

    def convert_pdf2png(self, dpi: int = 300) -> str:
        """Convert pdf to png"""
        zoom = dpi / 72  # zoom factor, standard: 72 dpi
        magnify = fitz.Matrix(zoom, zoom)
        doc = fitz.open(self.input_file_path)
        for page in doc:
            pix = page.get_pixmap(matrix=magnify)
            pix.save(f"{self.output_file_path}-{page.number}.png")
        logging.info(f"Success. File is saved in {self.output_file_path}")
        return True

    def convert(self) -> str:
        """Main convert function"""
        if self.ext == ".png":
            return self.convert_png2png()
        elif self.ext == ".heic":
            return self.convert_heic2png()
        elif self.ext == ".tiff":
            return self.convert_tiff2png()
        elif self.ext == ".pdf":
            return self.convert_pdf2png()
        else:
            logging.error("Error. File extension is not supported.")
            return False

# if __name__ == "__main__":
#     cvt = MyConverter(input_file_path="../test/testcases/test.tiff", output_file_path="out_test.png")
#     print(cvt.convert())
