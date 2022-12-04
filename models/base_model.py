from abc import ABC, abstractmethod

class AbstractFactoryModel(ABC):
    """
    TODO
    """

    def __init__(self, config, img):
        self.config = config
        self.img = img

    # super().__init__()
    
    
    @abstractmethod
    def fit(self):
        raise NotImplementedError
