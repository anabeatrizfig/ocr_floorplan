from .data_processing import AbstractFactoryDataPipeline
from IPython import embed


class DfPostprocessing(AbstractFactoryDataPipeline):
    """
    TODO
    """

    def __init__(self, path:str):
        self.path = path

#     def __init__(self, df):
#         self.df = df


#     def get_head(self):
#         return self.df.head()


# if __name__ == "__main__":
#     print('ok')

# # if __name__ == "__main__":
# #     df = DfPostprocessing(df=image2df(path='data/apt_01.jpg', process='simple'))
# #     embed()
# #     df.info()
