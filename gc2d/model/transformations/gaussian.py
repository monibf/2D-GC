
from scipy import ndimage

from .transform import Transform, TransformEnum

class Gaussian(Transform):
    
    def __init__(self, sigma):
        self.sigma = sigma
    
    
    def transform(self, data):
        return ndimage.gaussian_filter(data, self.sigma, mode='constant')

    def to_json(self):
        return {"Type" : TransformEnum.GAUSSIAN.name, "Data" : self.sigma}