from PyQt5.QtWidgets import QAction


class ToggleConvolutionAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        Toggles whether the model will return original or convolved data.
        :param model_wrapper: The model wrapper
        """
        super().__init__('Show transformed data', parent, checkable=True)
        self.model_wrapper = model_wrapper
        self.toggled.connect(self.toggle)
        self.setChecked(True)

    def toggle(self):
        self.model_wrapper.toggle_convolved(self.isChecked())
