
import tkinter as tk

class Renderer2d:
    
    def __init__(self, figure):
        self.figure = figure
    
    
    def update(self, data, clim=(1e4, 1e6)):
        """" Function to render a 2d numpy array to the frame belonging to this renderer """

        # TODO: Insert code to render graph
        # Should be done by calling a controller
        # ...
        
        self.figure.clear()
        axes = self.figure.add_axes((.1, .1, .8, .8))
        image = axes.imshow(data, clim=clim, origin="lower")
        self.figure.colorbar(image)
        print(dir(self.figure))

