from PyQt5.Qt import QColor, QPen
from enum import Enum, auto

class PreferenceEnum(Enum):
    SAVE_FILE = auto()
    PEN = auto()

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
        self.getter_map = {
            PreferenceEnum.SAVE_FILE : self.get_save_file,
            PreferenceEnum.PEN : self.get_pen
        }
        self.setter_map = {
            PreferenceEnum.SAVE_FILE : self.set_save_file,
            PreferenceEnum.PEN : self.set_pen
        }
        self.set_defaults()

    def set_defaults():
        self.pen[PenEnum.STYLE] = 1
        self.pen[PenEnum.WIDTH] = 4
        self.pen[PenEnum.COLOR] = "red"

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
        """ returns the set pen or the default, if pen is not set """
        return self.pen

    def set_pen(self, pen_dict):
        """ sets the default pen for roi drawing """
        for key in pen_dict:
            self.pen[key] = pen_dict[key]
        