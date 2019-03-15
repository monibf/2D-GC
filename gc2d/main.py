
from gc2d.MainWindow import MainWindow
from gc2d.render.renderer2d import Renderer2d
from gc2d.model.chromatograph import Chromatograph

def main():
    
    window = MainWindow()
    render = Renderer2d(window.graph_frame)
    chrom = Chromatograph.from_file("MF_AE3.txt")
    render.render2d(chrom.as_grid())
    
    window.top.mainloop()
    

