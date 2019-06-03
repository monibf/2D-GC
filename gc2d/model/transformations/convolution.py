
from scipy import ndimage

from .transform import Transform

class Convolution(Transform):
    
    def __init__(self, matrix):
        self.matrix = matrix
    
    def transform(self, data):
        if self.matrix is not None:
            return ndimage.convolve(data, weights=self.matrix, mode='constant')
        else:
            return data
    
    def to_json(self, data):
        return {
            "Type": "Convolution", # todo: update from enum once Oane's PR is merged
            "Matrix": self.matrix.tolist()
        }
