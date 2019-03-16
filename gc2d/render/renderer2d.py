
import tkinter as tk

class Renderer2d:
    
    def __init__(self, figure):
        self.figure = figure
        self.axes = None
    
    
    def update(self, data, clim=(1e4, 1e6)):
        """" Function to render a 2d numpy array to the frame belonging to this renderer """
        self.figure.clear()
        self.axes = self.figure.add_axes((.1, .1, .8, .8))
        image = self.axes.imshow(data, clim=clim, origin="lower")
        self.figure.colorbar(image)

