from PyQt5.QtWidgets import QAction, QFileDialog
from PyQt5.QtCore import QFile
import json

from gc2d.model.preferences import PreferenceEnum

class SavePrefsAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        A SavePrefsAction is a QAction that when triggered, saves the program preferences.
        It will open a file dialog to ask for a path, and save the preferences in *gcgc files in json format
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Save preferences', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.setStatusTip('Save preferences')
        self.triggered.connect(self.save)

    def save(self):
        """
        Asks for a path via a file dialog, Writes program preferences in the specified path as json format.
        :return: None
        """
        path = QFileDialog.getSaveFileName(self.window, 'Save GCxGC preferences', filter='GCxGC file (*.gcgc);; All files (*.*)')[0]
        if path is not '':
            _model, _integrations, preferences = self.model_wrapper.get_state()
            with open(path, 'w') as save_fd:
                json.dump({"preferences" : preferences}, 
                           save_fd, separators=(',', ':'), sort_keys=True, indent=4) 
        
