from datapipeline.preprocess.data_preprocessing import AbstractFactoryDataPipeline
from PIL import Image
from IPython import embed


class ImagePreprocessingSimple(AbstractFactoryDataPipeline):
    """
    TODO
    """


    def __init__(self, path:str):
        self.path = path
        self.image = Image.open(self.path)

    def get_path(self):
        return self.path

    def get_image(self):
        return self.image.show()

    def get_size(self):
        return self.image.size
    
    def run(self, resize_factor=1):
        image = self.image
        image = image.resize((image.size[0] * resize_factor, image.size[1] * resize_factor))
        return image


class ImagePreprocessingComplete(AbstractFactoryDataPipeline):
    """
    TODO
    """


    def __init__(self, path:str):
        self.path = path
        self.image = Image.open(self.path)

    def get_path(self):
        return self.path

    def get_image(self):
        return self.image.show()

    def get_size(self):
        return self.image.size

    def run(self):
        print('implement preprocess_complete')


if __name__ == "__main__":
    print('ok')
# if __name__ == "__main__":
#     obj = ImagePreprocessing(path = '../data/apt_01.jpg')
#     embed()
#     obj.get_image()
