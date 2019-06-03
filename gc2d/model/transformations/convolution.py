
from scipy import ndimage

from .transform import Transform

class Convolution(Transform):
    
    def __init__(self, matrix):
        self.matrix = matrix
    
    def transform(self, data):
        return ndimage.convolve(data, mode='constant')
    
    def to_json(self, data):
        return {
            "Type": "Convolution", # todo: update from enum once Oane's PR is merged
            "Matrix": self.matrix.tolist()
        }
