import tkinter as tk
from tkinter import filedialog
from math import floor, ceil

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.widgets import RectangleSelector

from gc2d.render.renderer2d import Renderer2d
from gc2d.model.chromatogram import Chromatogram


class MainWindow:
    """" The main window class. Creates and con the global components of the UI """

    def __init__(self):
        self.init_mainframe()
        
        self.renderer = Renderer2d(self.graph_figure)
        
        self.data = None
        
        self.rs = None

    def init_mainframe(self):
        """ Initialize the main frame. This includes every UI element """
        
        self.top = tk.Tk()

        self.top.title("GCxGC")

        self.init_frames()
        
        self.init_graph()
        
        self.select_button = tk.Button(self.left_frame, text="Select Region", command=self.select_integration)
        self.select_button.pack(side='top', fill="both")
        
        self.open_button = tk.Button(self.left_frame, text="Open Chromatogram data", command=self.load_chromatogram)
        self.open_button.pack(side='top', fill="both")


    def init_frames(self):
        
        toolbar_height = 40

        top_height = 480
        bottom_height = 80

        graph_width = 640
        sidebar_width = 100
        
        full_width = graph_width + sidebar_width
        
        self.toolbar_frame = tk.Frame(self.top, height=toolbar_height)
        self.toolbar_frame.pack(side='top', fill='both')
        self.toolbar_frame.pack_propagate(False)
        
        top_frame = tk.Frame(self.top, height=top_height, width=full_width, bg='gray')
        top_frame.pack(side='top')

        self.left_frame = tk.Frame(top_frame, height=top_height, width=sidebar_width, bg='darkgray')
        self.left_frame.pack(side='left')

        self.graph_frame = tk.Frame(top_frame, height=top_height, width=graph_width, bg='lightgray')
        self.graph_frame.pack(side='right')

        bottom_frame = tk.Frame(self.top, height=bottom_height, width=full_width, bg='gray26')
        bottom_frame.pack(side='bottom')
    
    
    def init_graph(self):
        
        self.graph_figure = Figure()
        
        # Create the canvas and put it on the graph_frame
        self.canvas = FigureCanvasTkAgg(self.graph_figure, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)
        self.toolbar.update()
        
        
    # End of init functions    
        
    
    
    def select_integration(self):
        print("starting selection")
        self.rs = RectangleSelector(self.renderer.axes, self.integrate,
                       drawtype='box', button=[1], minspanx=1, minspany=1,
                       spancoords='data')
        print(self.rs)
        
    def integrate(self, eclick, erelease):
        xmin = floor(min(eclick.xdata, erelease.xdata))
        ymin = floor(min(eclick.ydata, erelease.ydata))
        xmax = floor(max(eclick.xdata, erelease.xdata))
        ymax = floor(max(eclick.ydata, erelease.ydata))
        
        self.canvas.draw()
        print("integrating {} {}".format((xmin, ymin), (xmax, ymax)))
        if self.data is None:
            return
        data_part = self.data.as_grid()[xmin:xmax, ymin:ymax]
        total = data_part.sum()
        print(total, data_part.mean())
    
    
    def load_chromatogram(self, fname=None):
        if fname == None:
            fname = filedialog.askopenfilename()
        self.data = Chromatogram.from_file(fname)
        self.renderer.update(self.data.as_grid())
        self.canvas.draw()
    

