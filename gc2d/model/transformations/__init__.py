
import numpy

from .convolution import Convolution
from .dynamiccutoff import CutoffMode, DynamicCutoff
from .gaussian import Gaussian
from .min1d import Min1D
from .staticcutoff import StaticCutoff
from .transform import Transform, TransformEnum


def transform_from_json(json_dict):
    if "Type" not in json_dict:
        return None
    type = json_dict["Type"]
    if type == TransformEnum.NONE.name or "Data" not in json_dict:
        return Transform()
    elif type == TransformEnum.STATIC.name:
        return StaticCutoff(json_dict["Data"])
    elif type == TransformEnum.GAUSSIAN.name:
        return Gaussian(json_dict["Data"])
    elif type == TransformEnum.MIN1D.name:
        return Min1D(json_dict["Data"])
    elif type == TransformEnum.DYNAMIC.name and "Mode" in json_dict:
        return DynamicCutoff(json_dict["Data"], CutoffMode[json_dict["Mode"]])
    elif type == TransformEnum.CUSTOM.name:
        return Convolution(numpy.array(json_dict["Data"]))
    else:
        return None
