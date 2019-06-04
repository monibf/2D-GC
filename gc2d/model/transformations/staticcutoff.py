
from .transform import Transform, TransformEnum
from numpy import clip

class StaticCutoff(Transform):
    
    def __init__(self, cut_value):
        self.cut_value = cut_value
    
    def transform(self, data):
        return clip(data - self.cut_value, 0, None)

    def to_json(self):
        return {"Type" : TransformEnum.STATIC.name, "Data" : self.cut_value}