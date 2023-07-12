from PIL import Image
import pillow_heif
import os

class MyConverter: 
    def __init__(self):
        pass

    @staticmethod
    def file_extension(self, file_path: str) -> str:
        return os.path.splitext(file_path)[1]
    
    @staticmethod
    def convert_png2png(file_path: str) -> str:
        return file_path
    
    @staticmethod
    def convert_heic2png(file_path: str) -> str:
        heif_file = pillow_heif.read_heif(file_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
        
        )
        new_file_path = "./picture_name.png"
        image.save("./picture_name.png", format("png"))
        return new_file_path
    
    @staticmethod
    def convert_tiff2png(file_path: str) -> str:
        return file_path
    
    @staticmethod
    def convert_pdf2png(file_path: str) -> str:
        return file_path