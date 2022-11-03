import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'E:\Tesseract-OCR\tesseract.exe'

from IPython import embed
from datapipeline.image_processing import ImagePreprocessing
from datapipeline.df_postprocessing import DfPostprocessing

import warnings
warnings.filterwarnings("ignore")


def image2df(path, process='simple'):
    """
    process the image with tesseract and return DF
    """
    obj = ImagePreprocessing(path)

    if process == 'simple':
        obj = obj.preprocess_simple()
    elif process == 'complete':
        obj = obj.preprocess_complete()
    else:
        print('select a valid preprocess.')
    
    df = pytesseract.image_to_data(obj, output_type='data.frame')

    return df


def df2data(df, process='complete'):
    """
    transform df to readable data
    """
    df = DfPostprocessing(df)

    if process == 'simple':
        df = df.preprocess_simple()
    elif process == 'complete':
        df = df.preprocess_complete()
    else:
        print('select a valid preprocess.')
    
    return df


# if __name__ == '__main__':
#     print('ok')
if __name__ == "__main__":
    df = df2data(image2df(path='data/apt_02.jpg', process='simple'), process='complete')
    print(df['size'].sum(), 'm2')
    image = ImagePreprocessing(path='data/apt_02.jpg')
    image.get_image()
    # embed()
    print(df.head())
