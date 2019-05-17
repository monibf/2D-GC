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
        if path is '':
            return
        state = self.model_wrapper.get_state()
        extension = os.path.splitext(path)[1]
        save_fd = open(path, 'w')
        print(extension, "HEY")
        if extension == ".gcgc":
            print("saving full model ")
            json.dump({"model" : state[0].tolist(),
                       "integrations" : state[1],
                       "preferences" : state[2]},
                       save_fd, separators=(',', ':'), sort_keys=True, indent=4) 
        elif extension == ".gcgci":
            json.dump({"integrations" : state[1]}, 
                    save_fd, separators=(',', ':'), sort_keys=True, indent=4) 
        elif extension == ".gcgcp":
            json.dump({"preferences" : state[1]}, 
                    save_fd, separators=(',', ':'), sort_keys=True, indent=4) 
        save_fd.close()

    def get_path(self):
        path = self.model_wrapper.get_preference(PreferenceEnum.SAVE_FILE) 
        if path is None:
            path = QFileDialog.getSaveFileName(self.window, 'Save GCxGC', filter='Program(*.gcgc);;Integrations(*.gcgci);;Preferences(*.gcgcp)')[0]
            if os.path.splitext(path)[1] is ".gcgc": 
                self.model_wrapper.set_preference(PreferenceEnum.SAVE_FILE, path)
        return path 
