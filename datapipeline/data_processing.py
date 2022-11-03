from abc import ABC, abstractmethod

class AbstractFactoryDataPipeline(ABC):
    """
    TODO
    """
    
    @abstractmethod
    def preprocess_complete(self):
        pass
    
    @abstractmethod
    def preprocess_simple(self):
        pass


if __name__ == "__main__":
    print('ok')
    