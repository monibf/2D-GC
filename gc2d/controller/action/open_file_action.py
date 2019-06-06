from PyQt5.QtWidgets import QAction, QFileDialog
import numpy as np
import json


from gc2d.model.transformations import transform_from_json
from gc2d.controller.integration.selector import Selector
from gc2d.model.time_unit import TimeUnit
from gc2d.model.preferences import PreferenceEnum, PenEnum, ScaleEnum
from gc2d.model.palette.palette import Palette

class OpenFileAction(QAction):

    def __init__(self, parent, model_wrapper, shortcut=None):
        """
        An OpenFileAction is a QAction that when triggered, opens a QFileDialog to select a gcgc file to open. The
        The opening of the model is interpreted in this class.
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Open', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        if shortcut is not None:
            self.setShortcut(shortcut)
        self.setStatusTip('Open GCxGC file')
        self.triggered.connect(self.parse_file)

    def parse_file(self):
        """
        Show the Open file dialog, and interpret the data: 
        the model is overwritten, new selector objects are made for the integration area
        the program will save over this file, as the save_file preference is set to the selected path
        :return: None
        """
        file_name = QFileDialog.getOpenFileName(self.window, 'Open chromatography data', filter='GCxGC files (*.gcgc);; All files (*.*)')[0]
        if file_name:
            with open(file_name, 'r') as file:
                loaded = json.load(file)

            prefs_included = False
            if "preferences" in loaded:
                self.preload_prefs(loaded["preferences"])
                prefs_included = True

            if "model" in loaded:
                self.model_wrapper.set_model(np.array(loaded["model"]))
                self.model_wrapper.set_preference(PreferenceEnum.SAVE_FILE, file_name)

            if "integrations" in loaded and self.model_wrapper.model != None:
                for label, handles, pos in loaded["integrations"]:
                    Selector(self.model_wrapper, label, handles, pos)

            if prefs_included:
                self.postload_prefs(loaded["preferences"])

    def preload_prefs(self, preference_dict):
        if "PEN" not in preference_dict:
            return
        pen_dict = {}
        for property_type, value in preference_dict["PEN"].items():
            pen_dict[PenEnum[property_type]] = value
        self.model_wrapper.set_preference(PreferenceEnum.PEN, pen_dict)
                
    def postload_prefs(self, preference_json):
        if "TRANSFORM" in preference_json:
            self.load_transform(preference_json["TRANSFORM"])
        if "PALETTE" in preference_json:
            self.model_wrapper.set_palette(Palette(preference_json["PALETTE"]["Name"], preference_json["PALETTE"]["Colors"]))
        if "LOWER_BOUND" in preference_json:
            self.model_wrapper.set_lower_bound(preference_json["LOWER_BOUND"])
        if "UPPER_BOUND" in preference_json:
            self.model_wrapper.set_upper_bound(preference_json["UPPER_BOUND"])
        if "AXES" in preference_json:
            self.load_axes(preference_json["AXES"])
            


    def load_transform(self, transform_dict):
        transform = transform_from_json(transform_dict)
        if transform is not None:
            self.model_wrapper.set_transform(transform)
        
        
    def load_axes(self, axes_dict):
        for name in axes_dict:
            if name in {"X_UNIT", "Y_UNIT"}:
                self.model_wrapper.set_preference(ScaleEnum[name], TimeUnit[axes_dict[name]])
            else:
                self.model_wrapper.set_preference(ScaleEnum[name], axes_dict[name])