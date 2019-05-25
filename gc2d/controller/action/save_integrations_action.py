from PyQt5.QtWidgets import QAction, QFileDialog
from PyQt5.QtCore import QFile
import json
import os

from gc2d.model.preferences import PreferenceEnum

class SaveIntegrationsAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        A SaveIntegrationsAction is a QAction that when triggered, saves the integration areas.
        It will open a file dialog to ask for a path, and save the areas in *gcgc files in json format
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Save integration areas', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.setStatusTip('Save integration areas')
        self.triggered.connect(self.save)

    def save(self):
        """
        Asks for a path via a file dialog, Writes the integration areas in the specified path as json format.
        :param path: the path to write the data to
        :return: None
        """
        path = QFileDialog.getSaveFileName(self.window, 'Save GCxGC integrations', filter='GCxGC file (*.gcgc);; All files (*.*)')[0]
        if path is not '':
            state = self.model_wrapper.get_state()
            with open(path, 'w') as save_fd:
                json.dump({"integrations" : state[1]}, 
                           save_fd, separators=(',', ':'), sort_keys=True, indent=4) 
            
