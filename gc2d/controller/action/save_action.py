from PyQt5.QtWidgets import QAction, QFileDialog
from PyQt5.QtCore import QFile
import json

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
        self.triggered.connect(self.save)

    def save(self):
        """ 
        The implementation of saving. 
        Model state is saved in json format in a .gcgc file
        if no path is in preferences, a dialog will open
        :return: None
        """
        path = self.model_wrapper.get_preference(PreferenceEnum.SAVE_FILE) 
        if path is None:
            path = QFileDialog.getSaveFileName(self.window, 'Save GCxGC', filter='program state (*.gcgc))')[0]
            if path is '': # on cancel in file dialog
                return
            self.model_wrapper.set_preference(PreferenceEnum.SAVE_FILE, path) 
        save_fd = open(path, 'w')
        state = self.model_wrapper.get_state()
        json.dump({ "model" : state[0].tolist(),
                    "integrations" : state[1]}, 
                    save_fd, separators=(',', ':'), sort_keys=True, indent=4) 
        save_fd.close()

            
