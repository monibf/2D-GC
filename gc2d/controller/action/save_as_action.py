from PyQt5.QtWidgets import QAction

from gc2d.model.preferences import PreferenceEnum
from gc2d.controller.action.save_action import SaveAction

class SaveAsAction(QAction):

    def __init__(self, parent, model_wrapper, save_action):
        """
        An SaveAction is a QAction that when triggered, opens a QFileDialog to save the current state of the program. 
        The program state is serialized and saved in the specified file.
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Save As...', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.save_action = save_action # the implementation of saving which is called
        self.setShortcut('Ctrl+Shift+S')
        self.setStatusTip('Save As')
        self.triggered.connect(self.save)

    def save(self):
        self.model_wrapper.set_preference(PreferenceEnum.SAVE_FILE, None) 
        SaveAction.save(self.save_action) 

            
