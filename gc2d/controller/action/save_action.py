from PyQt5.QtWidgets import QAction, QFileDialog
from PyQt5.QtCore import QFile
import json

from gc2d.model.preferences import PreferenceEnum

class SaveAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        An SaveAction is a QAction that when triggered, opens a QFileDialog to save the current state of the program. 
        The program state is serialized and saved in the specified file.
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
        path = self.model_wrapper.get_preference(PreferenceEnum.SAVE_FILE) 
        if path is None:
            path = QFileDialog.getSaveFileName(self.window, 'Save GCxGC', filter='full state (*.gcgc);; integrations (*.gcgci);; preferences (*.gcgcp)')[0]
            if path is '':
                return
            self.model_wrapper.set_preference(PreferenceEnum.SAVE_FILE, path) 
        save_fd = open(path, 'w')
        state = self.model_wrapper.get_state()
        json.dump({ "model" : state[0].tolist(),
                    "integrations" : state[1]}, 
                    save_fd, separators=(',', ':'), sort_keys=True, indent=4) 
        save_fd.close()

            
