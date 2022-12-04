from enum import Enum
from .image_processing import ImagePreprocessingSimple, ImagePreprocessingComplete


class ImagePreprocess(Enum):
    """
    TODO
    """

    SIMPLE = ImagePreprocessingSimple
    COMPLETE = ImagePreprocessingComplete