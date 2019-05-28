from shutil import copy

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QWidget, \
    QFileDialog, QSizePolicy, QDialog, QFrame, QTreeView, QScrollArea, QSplitter
from PyQt5.QtCore import Qt

import gc2d.main as main
from gc2d.view.palette.palette import palettes, load_custom_palettes


class AllPreferences(QDialog):
    
    def __init__(self, parent, modelwrapper):
        """
        This window will open a palette chooser to let users select a palette from the (global) list of possible
        palettes.

        :param parent: The parent window, should be the current instance of MainWindow.
        :param modelwrapper: The wrapper of the model.
        """
        
        super().__init__(parent=parent)
        self.parent().addDialog(self)
        self.setWindowTitle("Preferences")

        self.modelwrapper = modelwrapper

        # vertical layout as central panel.
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)

        # h layout as at top panel
        topbox = QSplitter()
        topbox.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        vlayout.addWidget(topbox)

        # Tree View to view types of preferences.
        self.treeview = QTreeView()
        self.treeview.setMaximumWidth(100)
        self.treeview.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)
        topbox.addWidget(self.treeview)

        # scroll area to view preferences.
        self.scrollarea = QScrollArea()
        self.scrollarea.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        topbox.addWidget(self.scrollarea)

        # h layout as bottom panel (for buttons)
        bottombar = QWidget()
        bottombar.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        vlayout.addWidget(bottombar)

        bottomlayout = QHBoxLayout()
        bottombar.setLayout(bottomlayout)

        # cancel button
        cancelbutton = QPushButton('Cancel')
        bottomlayout.addWidget(cancelbutton, alignment=Qt.AlignLeft)
        cancelbutton.clicked.connect(self.close)

        glueapplysave = QWidget()
        bottomlayout.addWidget(glueapplysave, alignment=Qt.AlignRight)
        glueapplysave.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

        glueaplayout = QHBoxLayout()
        glueapplysave.setLayout(glueaplayout)

        # apply button
        applybutton = QPushButton('Apply')
        glueaplayout.addWidget(applybutton,)
        applybutton.clicked.connect(self.apply)

        # save button
        savebutton = QPushButton('Save')
        glueaplayout.addWidget(savebutton)
        savebutton.clicked.connect(self.save)

    def apply(self):
        """
        Applies the changed settings.
        :return: None
        """
        pass

    def save(self):
        """
        Applies the changed settings and closes the window.
        :return: None
        """
        self.apply()
        self.close()

    def closeEvent(self, event):
        """ Overrides the closing event to execute the on_close callback after closing.
        This is better than overriding close() because this will also execute when the user presses the x button on the
         top of the window."""
        event.accept()
        self.parent().dialogs.remove(self)
