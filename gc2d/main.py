from model.model_wrapper import ModelWrapper
from view.main_window import Window
from PyQt5.QtWidgets import QApplication
# import os.path

# from gc2d.mainwindow import MainWindow


def main():
    model_wrapper = ModelWrapper()
    app = QApplication([])
    window = Window(model_wrapper)
    app.exec()


    # window = MainWindow()
    # datafile = os.path.join(os.path.dirname(__file__), "..", "exampledata", "MF_AE3.txt")
    # window.load_chromatogram(datafile)
    
    # window.top.mainloop()
    

