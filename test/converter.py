from PIL import Image
import pyheif
import fitz
import shutil
import os

class MyConverter: 
    def __init__(self, input_file_path: str, output_file_path: str) -> None:
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.ext = self.file_extension()

    def file_extension(self) -> str:
        """
        determine the file extension
        """
        return os.path.splitext(self.input_file_path)[1]
    
    def convert_png2png(self) -> str:
        shutil.copyfile(self.input_file_path, self.output_file_path)
        return f"Success. File is saved in {self.output_file_path}"
    
    def convert_heic2png(self) -> str:
        heic_img = pyheif.read(self.input_file_path)
        image = Image.frombytes(
            heic_img.mode, 
            heic_img.size, 
            heic_img.data,
            "raw",
            heic_img.mode,
            heic_img.stride,
            )
        image.save("output.png")

        return f"Success. File is saved in {self.output_file_path}"

    def convert_tiff2png(self) -> str:
        im = Image.open(self.input_file_path)
        im.thumbnail(im.size)
        im.save(self.output_file_path, "png", quality=100)
        
        return f"Success. File is saved in {self.output_file_path}"
    
    def convert_pdf2png(self, dpi: int = 300) -> str:
        zoom = dpi / 72 # zoom factor, standard: 72 dpi
        magnify = fitz.Matrix(zoom, zoom) 
        doc = fitz.open(self.input_file_path) 
        for page in doc:
            pix = page.get_pixmap(matrix=magnify) 
            pix.save(f"{self.output_file_path}-{page.number}.png")
        return f"Success."
    
    def convert(self) -> str:
        """
        Main convert function
        """
        if self.ext == ".png":
            return self.convert_png2png()
        elif self.ext == ".heic":
            return self.convert_heic2png()
        elif self.ext == ".tiff":
            return self.convert_tiff2png()
        elif self.ext == ".pdf":
            return self.convert_pdf2png()
        else:
            return "Error. File extension is not supported."
        
# if __name__ == "__main__":
#     cvt = MyConverter(input_file_path="../test/testcases/test.tiff", output_file_path="out_test.png")
#     print(cvt.convert())
