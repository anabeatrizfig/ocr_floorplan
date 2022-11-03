from .data_processing import AbstractFactoryDataPipeline
from PIL import Image
from IPython import embed


class ImagePreprocessing(AbstractFactoryDataPipeline):
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

    def preprocess_complete(self):
        print('implement preprocess_complete')
    
    def preprocess_simple(self, resize_factor=1):
        image = self.image
        image = image.resize((image.size[0] * resize_factor, image.size[1] * resize_factor))
        return image

if __name__ == "__main__":
    print('ok')
# if __name__ == "__main__":
#     obj = ImagePreprocessing(path = '../data/apt_01.jpg')
#     embed()
#     obj.get_image()
