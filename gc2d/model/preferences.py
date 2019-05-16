from PyQt5.Qt import QColor, QPen
from enum import Enum

class PreferenceEnum(Enum):
    SAVE_FILE, PALETTE, PRECISION, PEN = range(4)


class Preferences:

    def __init__(self):
        """
        Container for all editable preferences. 
        The getters and setters are mapped based on the PreferenceEnum, 
        This was done to avoid code clutter in the model_wrapper and make the preferences easily iterable
        """
        self.save_file = None
        self.pen = None
        self.getter_map = {
            PreferenceEnum.SAVE_FILE : self.get_save_file,
            PreferenceEnum.PEN : self.get_pen
        }
        self.setter_map = {
            PreferenceEnum.SAVE_FILE : self.set_save_file,
            PreferenceEnum.PEN : self.set_pen
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
        if self.pen is None:
            self.pen = QPen()
            self.pen.setStyle(1)  # solid line
            self.pen.setWidth(4)
            self.pen.setColor(QColor("red"))
        return self.pen

    def set_pen(self, pen):
        self.pen = pen