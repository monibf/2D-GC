from PyQt5.Qt import QColor, QPen
from enum import Enum, auto
from gc2d.model.transformations import Transform
from gc2d.view.palette import palette

class PreferenceEnum(Enum):
    SAVE_FILE = auto()
    PEN = auto()
    TRANSFORM = auto()
    PALETTE = auto()

class PenEnum(Enum):
    COLOR = auto()
    WIDTH = auto()
    STYLE = auto()


class Preferences:

    def __init__(self):
        """
        Container for all editable preferences. 
        The getters and setters are mapped based on the PreferenceEnum, 
        This was done to avoid code clutter in the model_wrapper and make the preferences easily iterable
        """
        self.save_file = None
        self.pen = {}
        self.transform = Transform()
        self.palette = palette.viridis.getColors()
        self.getter_map = {
            PreferenceEnum.SAVE_FILE : self.get_save_file,
            PreferenceEnum.PEN : self.get_pen
        }
        self.setter_map = {
            PreferenceEnum.SAVE_FILE : self.set_save_file,
            PreferenceEnum.PEN : self.set_pen,
            PreferenceEnum.TRANSFORM : self.set_transform,
            PreferenceEnum.PALETTE : self.set_palette
        }
        self.set_defaults()

    def set_defaults(self):
        """ Constructs the default pen dictionary """
        self.pen[PenEnum.STYLE] = 1
        self.pen[PenEnum.WIDTH] = 4
        self.pen[PenEnum.COLOR] = "red"
    
    def get_state(self):
        return {
            "PEN": {enum.name: self.pen[enum] for enum in PenEnum},
            "TRANSFORM" : self.transform.to_json(),
            "PALETTE" : self.palette.tolist()
        }

    def get(self, which):
        """
        returns a specifiable variable in preferences
        :param which: a PreferenceEnum object specifying which preference should be retrieved
        :return: the specified preference value
        """
        return self.getter_map[which]()

    def set(self, which, value):
        """
        Sets a preference value, specified by which
        :param which: a PreferenceEnum object specifying which preference should be overwritten
        :return: None
        """
        self.setter_map[which](value)

    def get_save_file(self):
        """ returns the save file path """
        return self.save_file

    def set_save_file(self, path):
        """ sets the save file path """
        self.save_file = path
    
    def get_pen(self):
        """ constructs and returns the set pen  """
        pen = QPen()
        pen.setWidth(self.pen[PenEnum.WIDTH])
        pen.setColor(QColor(self.pen[PenEnum.COLOR]))
        pen.setStyle(self.pen[PenEnum.STYLE])
        return pen

    def set_pen(self, pen_dict):
        """ 
        Sets pen preferences to specified values. 
        Can either set all preferences, or one as specified in the supplied dictionary
        :param pen_dict: a dictionary of one or multiple fields of the form {PenEnum.(spec) : value}
        """
        for key in pen_dict:
            self.pen[key] = pen_dict[key]

    def set_transform(self, transform):
        self.transform = transform

    def set_palette(self, colors):
        self.palette = colors