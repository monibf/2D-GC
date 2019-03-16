import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class MainWindow:
    """" The main window class. Creates and con the global components of the UI """

    def __init__(self):
        self.top = tk.Tk()
        self.init_mainframe()

    def init_mainframe(self):
        """ Initialize the main frame. This includes every UI element """
        
        toolbar_height = 50

        top_height = 480
        bottom_height = 80

        graph_width = 640
        sidebar_width = 100

        self.top.title("GCxGC")

        self.init_toolbar_frame(toolbar_height)
        self.init_top_frame(frame_height=top_height, graph_width=graph_width, sidebar_width=sidebar_width)
        self.init_bottom_frame(frame_height=bottom_height, frame_width=graph_width + sidebar_width)
        
        self.init_graph()


    def init_toolbar_frame(self, toolbar_height):
        
        self.toolbar_frame = tk.Frame(self.top, height=toolbar_height)
        self.toolbar_frame.pack(side='top', fill='both')

    def init_top_frame(self, frame_height, graph_width, sidebar_width):
        """" Initialize the top frame. This includes the graph and graph control frame """
        

        top_frame = tk.Frame(self.top, height=frame_height, width=graph_width + sidebar_width, bg='gray')
        top_frame.pack(side='top')

        self.left_frame = tk.Frame(top_frame, height=frame_height, width=sidebar_width, bg='darkgray')
        self.left_frame.pack(side='left')

        self.graph_frame = tk.Frame(top_frame, height=frame_height, width=graph_width, bg='lightgray')
        self.graph_frame.pack(side='right')
        

    def init_bottom_frame(self, frame_height, frame_width):
        """" Initialize the top frame. This includes other controls """

        bottom_frame = tk.Frame(self.top, height=frame_height, width=frame_width, bg='gray26')
        bottom_frame.pack(side='bottom')
    
    
    def init_graph(self):
        
        self.graph_figure = Figure()
        
        # Create the canvas and put it on the graph_frame
        self.canvas = FigureCanvasTkAgg(self.graph_figure, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)
        self.toolbar.update()

