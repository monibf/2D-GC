from enum import Enum, auto


class Transform:
        
    def transform(self, data):
        return data.copy()

    def to_json(self):
        return {"Type" : TransformEnum.NONE.name}

class TransformEnum(Enum):
    NONE = auto()
    DYNAMIC = auto()
    GAUSSIAN = auto()
    STATIC = auto()
    CUSTOM = auto()
