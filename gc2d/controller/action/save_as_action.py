from gc2d.controller.action.save_action import SaveAction
from gc2d.model.preferences import PreferenceEnum


class SaveAsAction(SaveAction):

    def __init__(self, parent, model_wrapper, shortcut=None):
        """
        A SaveAsAction is a QAction that when triggered, opens a QFileDialog to save the current state of the program. 
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__(parent, model_wrapper, shortcut)
        self.setText('Save As...')
        self.setStatusTip('Save As')

    def save(self):
        """"
        Sets save file to None and calls save_action
        Because the save_file path is None, the SaveAction will ask for a new path via a dialog
        :return: None
        """
        self.model_wrapper.set_preference(PreferenceEnum.SAVE_FILE, None)
        super().save()
