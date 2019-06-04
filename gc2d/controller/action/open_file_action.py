from PyQt5.QtWidgets import QAction, QFileDialog
import os.path
import numpy as np
import json


from gc2d.model.transformations import Transform, Gaussian, StaticCutoff, DynamicCutoff, Min1D
from gc2d.model.transformations.dynamiccutoff import CutoffMode
from gc2d.controller.integration.selector import Selector
from gc2d.model.preferences import PreferenceEnum, PenEnum
from gc2d.view.palette.palette import Palette

class OpenFileAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        An OpenFileAction is a QAction that when triggered, opens a QFileDialog to select a gcgc file to open. The
        The opening of the model is interpreted in this class.
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Open', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.setShortcut('Ctrl+O')
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
        pen_dict = {}
        for property_type, value in preference_dict["PEN"].items():
            pen_dict[PenEnum[property_type]] = value
        self.model_wrapper.set_preference(PreferenceEnum.PEN, pen_dict)
                
    def postload_prefs(self, preference_json):
        self.load_transform(preference_json["TRANSFORM"])
        self.model_wrapper.set_palette(Palette(preference_json["PALETTE"]["Name"], preference_json["PALETTE"]["Colors"]))
        self.model_wrapper.set_lower_bound(preference_json["LOWER_BOUND"])
        self.model_wrapper.set_upper_bound(preference_json["UPPER_BOUND"])

    def load_transform(self, transform_dict):
        type = transform_dict["Type"]
        if type == "NONE":
            self.model_wrapper.set_transform(Transform())
        elif type == "STATIC":
            self.model_wrapper.set_transform(StaticCutoff(transform_dict["Data"]))
        elif type == "DYNAMIC":
            self.model_wrapper.set_transform(DynamicCutoff(transform_dict["Data"], CutoffMode[transform_dict["Mode"]]))
        elif type == "GAUSSIAN":
            self.model_wrapper.set_transform(Gaussian(transform_dict["Data"]))
        elif type == "MIN1D":
            self.model_wrapper.set_transform(Min1D(transform_dict["Data"]))

        