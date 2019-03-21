from PyQt5.QtWidgets import QMainWindow
from controller.exit_button import ExitButton
from controller.open_button import OpenButton


class Window(QMainWindow):

    def __init__(self, model_wrapper):
        super().__init__()

        """"""
        self.model_wrapper = model_wrapper
        self.resize(250, 150)
        self.setWindowTitle('GCxGC')
        self.create_menus()
        self.show()

    def create_menus(self):
        """
        Creates the Tool bar menus; file, edit, help, etc.
        :return: None
        """

        main_menu = self.menuBar()

        file_menu = main_menu.addMenu('File')
        file_menu.addAction(OpenButton(self, self.model_wrapper))
        file_menu.addAction(ExitButton(self))

        editMenu = main_menu.addMenu('Edit')
        # TODO

        viewMenu = main_menu.addMenu('View')
        # TODO

        toolsMenu = main_menu.addMenu('Tools')
        # TODO

        helpMenu = main_menu.addMenu('Help')
        # TODO
