from PIL import Image, ImageSequenceimport
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
        im = Image.open(file_path)
        new_file_path = None
        for i, page in enumerate(ImageSequence.Iterator(im)):
            page.mode = 'I'
            new_file_path = str(i) + '.png'
            page.point(lambda i:i*(1./256)).convert('L').save(new_file_path)
        return new_file_path
    
    @staticmethod
    def convert_pdf2png(file_path: str) -> str:
        return file_path