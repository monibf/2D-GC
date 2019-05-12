from PyQt5.QtWidgets import QAction, QFileDialog
from PyQt5.QtCore import QFile
import json

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
        self.triggered.connect(self.show_dialog)

    def show_dialog(self):
        """
        Show the Save file dialog.
        :return: None
        """
        path = QFileDialog.getSaveFileName(self.window, 'Save GCxGC', filter='full state (*.gcgc);; integrations (*.gcgci);; preferences (*.gcgcp)')
        if path[0] != '':
            save_fd = open(path[0], 'w')
            state = self.model_wrapper.get_state()
            print(state[0])
            json.dump({ "model" : state[0].tolist(),
                        "integrations" : state[1]}, 
                        save_fd, separators=(',', ':'), sort_keys=True, indent=4) 
            save_fd.close()
            
