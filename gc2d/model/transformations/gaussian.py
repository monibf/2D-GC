
from scipy import ndimage

from .transform import Transform

class Gaussian(Transform):
    
    def __init__(self, sigma):
        self.sigma = sigma
    
    
    def transform(self, data):
        return ndimage.gaussian_filter(data, self.sigma, mode='constant')
