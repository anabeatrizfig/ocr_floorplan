class Config(object):
    """
    TODO
    """

    def __init__(self):

        self.selected_model:str = 'PYTESSERACT'
        self.preprocess_pipeline = 'SIMPLE'
        self.postprocess_pipeline = 'COMPLETE'
        self.test_img = 'data/apt_02.jpg'
