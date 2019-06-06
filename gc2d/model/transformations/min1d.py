
import numpy as np
from scipy import ndimage

from .transform import Transform, TransformEnum


class Min1D(Transform):
    
    def __init__(self, size):
        self.size = size

    def transform(self, data):
        filtered_1d = ndimage.minimum_filter(np.sum(a=data, axis=1), self.size)/data.shape[1]
        mask_2d = np.tile(filtered_1d, (data.shape[1], 1)).transpose()
        return data-mask_2d

    def to_json(self):
        return {"Type" : TransformEnum.MIN1D.name, "Data" : self.size}
