from abc import ABC, abstractmethod
from enum import Enum, unique
from models.pytesseract_model import PytesseractModel
# from utils.enums import ExtendedEnum

class OpticalRecognizerModels(Enum):
    """
    TODO
    """

    PYTESSERACT = PytesseractModel