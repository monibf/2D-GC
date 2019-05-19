from PyQt5.QtWidgets import QAction, QFileDialog
from PyQt5.QtCore import QFile
import json
import os

from gc2d.model.preferences import PreferenceEnum

class SaveAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        A SaveAction is a QAction that when triggered, saves the program state in the save_file specified in preferences.
        If no file is specified (as with new imported data, or after Save As), it will open a file dialog to specify this. 
        The essential parts of the program state (model data, integration areas) are saved as text in json format
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Save', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.setShortcut('Ctrl+S')
        self.setStatusTip('Save')
        self.triggered.connect(lambda: self.dump(self.get_path()))

    def dump(self, path):
        """
        Writes (parts of) the model state in the specified path as json format.
        If *.gcgc, the complete model state will be written.
        If *.gcgci, only the integration areas will be written.
        If *.gcgcp, only preferences will be written. 
        :param path: the path to write the data to
        :return: None
        """
        if path is '':
            return
        state = self.model_wrapper.get_state()
        extension = os.path.splitext(path)[1]
        save_fd = open(path, 'w')
        if extension == ".gcgc":
            json.dump({"model" : state[0].tolist(),
                       "integrations" : state[1],
                       "preferences" : state[2]},
                       save_fd, separators=(',', ':'), sort_keys=True, indent=4) 
        elif extension == ".gcgci":
            json.dump({"integrations" : state[1]}, 
                       save_fd, separators=(',', ':'), sort_keys=True, indent=4) 
        elif extension == ".gcgcp":
            json.dump({"preferences" : state[2]}, 
                       save_fd, separators=(',', ':'), sort_keys=True, indent=4) 
        save_fd.close()

    def get_path(self):
        """
        Tries to find if this file was loaded from a *.gcgc file (in preferences), if so -> returns that path
        Else opens a dialog to assign a new save path, or only save the integrations and preferences.
        :return path: The path to save the data in.
        """
        path = self.model_wrapper.get_preference(PreferenceEnum.SAVE_FILE) 
        if path is None:
            path = QFileDialog.getSaveFileName(self.window, 'Save GCxGC', filter='Program(*.gcgc);;Integrations(*.gcgci);;Preferences(*.gcgcp)')[0]
            if os.path.splitext(path)[1] is ".gcgc": 
                self.model_wrapper.set_preference(PreferenceEnum.SAVE_FILE, path)
        return path 
