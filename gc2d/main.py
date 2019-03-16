
import os.path

from gc2d.MainWindow import MainWindow
from gc2d.render.renderer2d import Renderer2d
from gc2d.model.chromatogram import Chromatogram


def main():
    
    window = MainWindow()
    render = Renderer2d(window.graph_figure)
    datafile = os.path.join(os.path.dirname(__file__), "MF_AE3.txt")
    chrom = Chromatogram.from_file(datafile)
    render.update(chrom.as_grid())
    #window.canvas.draw()
    
    window.top.mainloop()
    

