
import numpy as np

from .transform import Transform

from enum import Enum

class CutoffMode(Enum):
    MEAN = "MEAN"
    QUANTILE = "QUANTILE"

class DynamicCutoff:
    
    def __init__(self, percentile, mode=CutoffMode.MEAN):
        self.quantile = percentile / 100
        self.mode = mode
    
    def transform(self, data):
        data = np.clip(data, 0, None)
        quantiles = np.quantile(data, self.quantile, axis=1)
        if self.mode == CutoffMode.MEAN:
            quantiles = quantiles.reshape((len(quantiles), 1))
            mask = data <= quantiles
            averages = np.average(data, axis=1, weights=mask)
            cutoffs = averages
        elif self.mode == CutoffMode.QUANTILE:
            cutoffs = quantiles
        else:
            raise ValueError("unknown cut-off mode '{}'".format(mode))
        return np.clip((data.transpose() - cutoffs).transpose(), 0, None)
        
