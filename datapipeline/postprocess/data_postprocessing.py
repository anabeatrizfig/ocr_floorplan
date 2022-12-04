from abc import ABC, abstractmethod

class AbstractFactoryDataPipeline(ABC):
    """
    TODO
    """
    
    @abstractmethod
    def run(self):
        pass


if __name__ == "__main__":
    print('ok')
    