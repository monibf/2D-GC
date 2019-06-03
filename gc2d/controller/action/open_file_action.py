from PyQt5.QtWidgets import QAction, QFileDialog
import os.path
import numpy as np
import json

from gc2d.model.transformations import Transform, Gaussian, StaticCutoff, DynamicCutoff
from gc2d.model.transformations.dynamiccutoff import CutoffMode

from gc2d.controller.integration.selector import Selector
from gc2d.model.preferences import PreferenceEnum, PenEnum

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

            if "preferences" in loaded:
                self.parse_preferences(loaded["preferences"].items())

            if "model" in loaded:
                self.model_wrapper.set_model(np.array(loaded["model"]))
                self.model_wrapper.set_preference(PreferenceEnum.SAVE_FILE, file_name)

            if "integrations" in loaded and self.model_wrapper.model != None:
                for label, handles, pos in loaded["integrations"]:
                    Selector(self.model_wrapper, label, handles, pos)

                
    def parse_preferences(self, preference_json):
        for pref, val in preference_json:   
            if pref == "PEN":
                # construct pen dictionary to overwrite defaults; not all fields of PenEnum need to be specified
                pen_dict = {}
                for property_type, value in val.items():
                    pen_dict[PenEnum[property_type]] = value
                self.model_wrapper.set_preference(PreferenceEnum.PEN, pen_dict)

            if pref == "TRANSFORM":
                if val["Type"] == "NONE":
                    self.model_wrapper.set_transform(Transform())
                elif val["Type"] == "STATIC":
                    self.model_wrapper.set_transform(StaticCutoff(val["Data"]))
                elif val["Type"] == "DYNAMIC":
                    self.model_wrapper.set_transform(DynamicCutoff(val["Data"], CutoffMode[val["Mode"]]))
                elif val["Type"] == "GAUSSIAN":
                    self.model_wrapper.set_transform(Gaussian(val["Data"]))