
import numpy as np

from .transform import Transform

class DynamicCutoff:
    
    def __init__(self, percentile):
        self.quantile = percentile / 100
    
    def transform(self, data):
        data = np.clip(data, 0, None)
        quantiles = np.quantile(data, self.quantile, axis=1)
        quantiles = quantiles.reshape((len(quantiles), 1))
        mask = data <= quantiles
        averages = np.average(data, axis=1, weights=mask)
        return (data.transpose() - averages).transpose()
        
