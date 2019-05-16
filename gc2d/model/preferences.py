from enum import Enum

class PreferenceEnum(Enum):
    SAVE_FILE, PALETTE, PRECISION = range(3)


class Preferences:

    def __init__(self):
        """
        Container for all editable preferences
        """
        self.save_file = None
        self.getter_map = {
            PreferenceEnum.SAVE_FILE : self.get_save_file
        }
        self.setter_map = {
            PreferenceEnum.SAVE_FILE : self.set_save_file
        }


    def get(self, which):
        return self.getter_map[which]()

    def set(self, which, value):
        self.setter_map[which](value)

    def get_save_file(self):
        return self.save_file

    def set_save_file(self, path):
        self.save_file = path
    