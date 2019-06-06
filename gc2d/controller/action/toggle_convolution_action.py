from PyQt5.QtWidgets import QAction


class ToggleConvolutionAction(QAction):

    def __init__(self, parent, model_wrapper, shortcut=None):
        """
        Toggles whether the model will return original or convolved data.
        :param model_wrapper: The model wrapper
        """
        super().__init__('Show transformed data', parent, checkable=True)
        self.model_wrapper = model_wrapper
        self.toggled.connect(self.update)
        if shortcut is not None:
            self.setShortcut(shortcut)
        self.setEnabled(self.model_wrapper.model is not None)
        self.model_wrapper.add_observer(self, self.notified)

        self.setChecked(True)

    def update(self):
        if self.model_wrapper.model is not None:
            self.model_wrapper.toggle_convolved(self.isChecked())
    
    def notified(self, name, model):
        if name == 'model':
            self.setEnabled(model is not None)
            self.update()
