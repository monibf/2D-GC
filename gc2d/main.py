
import os.path

from gc2d.MainWindow import MainWindow
from gc2d.render.renderer2d import Renderer2d
from gc2d.model.chromatogram import Chromatogram


def main():
    
    window = MainWindow()
    render = Renderer2d(window.graph_frame)
    datafile = os.path.join(os.path.dirname(__file__), "MF_AE3.txt")
    chrom = Chromatogram.from_file(datafile)
    render.render2d(chrom.as_grid())
    
    window.top.mainloop()
    

