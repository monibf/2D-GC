from PyQt5.QtWidgets import QAction, QFileDialog
import os

from gc2d.model.preferences import PreferenceEnum
from gc2d.controller.action.save_action import SaveAction

class SaveAsAction(QAction):

    def __init__(self, parent, model_wrapper, save_action):
        """
        A SaveAsAction is a QAction that when triggered, opens a QFileDialog to save the current state of the program. 
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        :param save_action: a SaveAction object, which handles the actual saving
        """
        super().__init__('Save As...', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.save_action = save_action # the implementation of saving which is called
        self.setShortcut('Ctrl+Shift+S')
        self.setStatusTip('Save As')
        self.triggered.connect(self.save)

    def save(self):
        """"
        Sets the save_file path in the preferences to None and calls a regular save call in save_action.
        Because the save_file path is None, the SaveAction will ask for a new path via a dialog
        :return: None
        """
        self.model_wrapper.set_preference(PreferenceEnum.SAVE_FILE, None) 
        SaveAction.dump(self.save_action, self.get_path()) 

    def get_path(self):
        """
        Opens a dialog for a new save path for either program, integrations, or preferences, with different extensions.
        :return path: the path to save data to
        """
        path = QFileDialog.getSaveFileName(self.window, 'Save GCxGC', filter='Program(*.gcgc));;Integrations(*.gcgci);;Preferences(*.gcgcp)')[0]
        if os.path.splitext(path)[1] is ".gcgc": 
            self.model_wrapper.set_preference(PreferenceEnum.SAVE_FILE, path)
        return path 