from PyQt5.QtWidgets import QAction


class ToggleDisregardNegativesAction(QAction):

    def __init__(self, parent, model_wrapper, shortcut=None):
        """
        Toggles whether the integrations will  take the negative values into account in their calculations
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
            self.model_wrapper.toggle_disregard_negatives(self.isChecked())

    def notified(self, name, model):
        if name == 'model':
            self.setEnabled(model is not None)
            self.update()
