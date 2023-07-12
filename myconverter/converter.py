from Pil import Image
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
        return file_path
    
    @staticmethod
    def convert_tiff2png(file_path: str) -> str:
        return file_path
    
    @staticmethod
    def convert_pdf2png(file_path: str) -> str:
        return file_path