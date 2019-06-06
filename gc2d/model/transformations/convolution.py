from scipy import ndimage

from .transform import Transform, TransformEnum


class Convolution(Transform):

    def __init__(self, matrix):
        self.matrix = matrix

    def transform(self, data):
        if self.matrix is not None:
            return ndimage.convolve(data, weights=self.matrix, mode='constant')
        else:
            return data

    def to_json(self):
        return {
            "Type": TransformEnum.CUSTOM.name,
            "Data": self.matrix.tolist()
        }
