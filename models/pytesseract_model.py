from models.base_model import AbstractFactoryModel
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'E:\Tesseract-OCR\tesseract.exe'


class PytesseractModel(AbstractFactoryModel):

    """_summary_

    Args:
        AbstractFactoryModel (_type_): _description_
    """

    def __init__(self, config, img):

        self.img = img
        self.config = config


    def fit(self):

        df_raw = pytesseract.image_to_data(self.img, output_type='data.frame')

        return df_raw
