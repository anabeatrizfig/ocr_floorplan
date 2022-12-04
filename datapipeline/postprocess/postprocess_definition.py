from enum import Enum
from .df_postprocessing import DfPostprocessingSimple, DfPostprocessingComplete


class DfPostprocess(Enum):
    """
    TODO
    """

    SIMPLE = DfPostprocessingSimple
    COMPLETE = DfPostprocessingComplete