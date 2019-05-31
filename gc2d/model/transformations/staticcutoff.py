
from .transform import Transform
from numpy import clip

class StaticCutoff(Transform):
    
    def __init__(self, cut_value):
        self.cut_value = cut_value
    
    def transform(self, data):
        return clip(data - self.cut_value, 0, None)
