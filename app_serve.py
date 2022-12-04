from IPython import embed
from config.base_config import Config
from models.models_definition import OpticalRecognizerModels
from datapipeline.preprocess.preprocess_definition import ImagePreprocess
from datapipeline.postprocess.postprocess_definition import DfPostprocess
import warnings
import logging
import os
import pandas as pd

logger = logging.getLogger(__name__)


warnings.filterwarnings('ignore')

config = Config()

# preprocess
def preprocess(path):
    selected_preprocesser = ImagePreprocess[config.preprocess_pipeline].value

    img = selected_preprocesser(path).run()

    logger.info('preprocessing is done!')

    return img


# infer
def predict(img):

    logger.info('prediction begin!')
   
    selected_model = OpticalRecognizerModels[config.selected_model].value

    df_raw = selected_model(config = config, img = img).fit()

    logger.info('prediction is done!')


    return df_raw


# postprocess
def postprocess(df_raw):
    selected_postprocesser = DfPostprocess[config.postprocess_pipeline].value

    df = selected_postprocesser(df_raw).run()

    return df

def main():

    df = pd.DataFrame(columns=['file', 'room', 'side_a', 'side_b', 'size'])
    
    word_dir = os.listdir('data/')
    for files in word_dir:
        img_raw = preprocess(path = os.path.join('data/', files))
        df_raw = predict(img = img_raw)
        df_file = postprocess(df_raw)

        df_file['file'] = str(files)

        df = pd.concat([df, df_file])

    return df

    # print('ok')
if __name__ == "__main__":
    
    df = main()
    print(df)
