from enum import Enum, auto

from PyQt5.Qt import QColor, QPen

from gc2d.model.palette import palette
from gc2d.model.time_unit import TimeUnit
from gc2d.model.transformations import Transform


class PreferenceEnum(Enum):
    SAVE_FILE = auto()
    PEN = auto()
    TRANSFORM = auto()
    PALETTE = auto()
    LOWER_BOUND = auto()
    UPPER_BOUND = auto()


class PenEnum(Enum):
    COLOR = auto()
    WIDTH = auto()
    STYLE = auto()


class ScaleEnum(Enum):
    X_UNIT = auto()
    Y_UNIT = auto()
    Y_UNIT_1D = auto()
    X_PERIOD = auto()
    Y_PERIOD = auto()


class Preferences:

    def __init__(self):
        """
        Container for all editable preferences. 
        The getters and setters are mapped based on the PreferenceEnum, 
        This was done to avoid code clutter in the model_wrapper and make the preferences easily iterable
        """
        self.save_file = None
        self.pen = {}

        self.x_unit = TimeUnit.NONE
        self.y_unit = TimeUnit.NONE
        self.y_unit_1d = 'ppm'
        
        self.x_period = 0
        self.y_period = 0
        
        self.transform = Transform()
        self.palette = palette.viridis
        # bounds are written when a model is loaded
        self.lower_bound = None
        self.upper_bound = None

        self.getter_map = {
            PreferenceEnum.SAVE_FILE : self.get_save_file,
            PreferenceEnum.PEN : self.get_pen,
            ScaleEnum.X_UNIT: self.get_x_unit,
            ScaleEnum.Y_UNIT: self.get_y_unit,
            ScaleEnum.Y_UNIT_1D: self.get_y_unit_1d,
            ScaleEnum.X_PERIOD: self.get_x_period,
            ScaleEnum.Y_PERIOD: self.get_y_period,
            PreferenceEnum.PALETTE : self.get_palette
        }
        self.setter_map = {
            PreferenceEnum.SAVE_FILE : self.set_save_file,
            PreferenceEnum.PEN : self.set_pen,
            ScaleEnum.X_UNIT: self.set_x_unit,
            ScaleEnum.Y_UNIT: self.set_y_unit,
            ScaleEnum.Y_UNIT_1D: self.set_y_unit_1d,
            ScaleEnum.X_PERIOD: self.set_x_period,
            ScaleEnum.Y_PERIOD: self.set_y_period,
            PreferenceEnum.TRANSFORM : self.set_transform,
            PreferenceEnum.PALETTE : self.set_palette,
            PreferenceEnum.LOWER_BOUND : self.set_lower_bound,
            PreferenceEnum.UPPER_BOUND : self.set_upper_bound
        }
        self.set_defaults()

    def set_defaults(self):
        """ Constructs the default pen dictionary """
        self.pen[PenEnum.STYLE] = 1
        self.pen[PenEnum.WIDTH] = 4
        self.pen[PenEnum.COLOR] = "red"
    
    def get_state(self):
        """ return a json serializable preferences state """
        state = {}
        state["PEN"] = {enum.name: self.pen[enum] for enum in PenEnum}
        state["TRANSFORM"] = self.transform.to_json()
        state["PALETTE"] = {"Colors" : self.palette.getColors().tolist(), "Name": self.palette.name}
        state["AXES"] = {enum.name : self.get(enum) for enum in ScaleEnum if enum not in {ScaleEnum.X_UNIT, ScaleEnum.Y_UNIT}}
        state["AXES"]["X_UNIT"] = self.get_x_unit().name
        state["AXES"]["Y_UNIT"] = self.get_y_unit().name
        state["UPPER_BOUND"] = self.upper_bound
        state["LOWER_BOUND"] = self.lower_bound
        return state

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
            
    def get_x_unit(self):
        """
        :return: the unit of the x axis
        """
        return self.x_unit

    def set_x_unit(self, unit):
        """
        Sets the unit of the x axis
        :param unit: The unit the should be x axis
        :return: None
        """
        self.x_unit = unit

    def get_y_unit(self):
        """
        :return: the unit of the y axis
        """
        return self.y_unit

    def set_y_unit(self, unit):
        """
        Sets the unit of the y axis
        :param unit: The unit the should be y axis
        :return: None
        """
        self.y_unit = unit

    def get_y_unit_1d(self):
        """
        :return: the unit of the y axis in 1d
        """
        return self.y_unit_1d

    def set_y_unit_1d(self, unit):
        """
        Sets the unit of the y axis in 1d
        :param unit: The unit the should be y axis
        :return: None
        """
        self.y_unit_1d = unit

    def get_x_period(self):
        """
        :return: the period of the x axis
        """
        return self.x_period

    def set_x_period(self, period):
        """
        Sets the period of the x axis
        :param period: The period the should be x axis
        :return: None
        """
        self.x_period = period

    def get_y_period(self):
        """
        :return: the period of the y axis
        """
        return self.y_period

    def set_y_period(self, period):
        """
        Sets the period of the y axis
        :param period: The period the should be y axis
        :return: None
        """
        self.y_period = period

    def set_transform(self, transform):
        self.transform = transform

    def set_palette(self, palette):
        self.palette = palette
    
    def get_palette(self):
        return self.palette
        
    def set_lower_bound(self, lower_bound):
        self.lower_bound = lower_bound
    
    def set_upper_bound(self, upper_bound):
        self.upper_bound = upper_bound
