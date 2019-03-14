import Tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class MainWindow:
    """" The main window class. Creates and con the global components of the UI """
    top = tk.Tk()

    def __init__(self):
        self.init_mainframe()

    def init_mainframe(self):
        """ Initialize the main frame. This includes every UI element """

        top_height = 480
        bottom_height = 80

        graph_width = 640
        sidebar_width = 100

        self.top.title("2Dx2D GC")

        self.init_top_frame(frame_height=top_height, graph_width=graph_width, sidebar_width=sidebar_width)
        self.init_bottom_frame(frame_height=bottom_height, frame_width=graph_width + sidebar_width)

        self.render2D()
        self.top.mainloop()

    def init_top_frame(self, frame_height, graph_width, sidebar_width):
        """" Initialize the top frame. This includes the graph and graph control frame """

        top_frame = tk.Frame(self.top, height=frame_height, width=graph_width + sidebar_width, bg='gray')
        top_frame.pack(side='top')

        left_frame = tk.Frame(top_frame, height=frame_height, width=sidebar_width, bg='darkgray')
        left_frame.pack(side='left')

        graph_frame = tk.Frame(top_frame, height=frame_height, width=graph_width, bg='lightgray')
        graph_frame.pack(side='right')

    def init_bottom_frame(self, frame_height, frame_width):
        """" Initialize the top frame. This includes other controls """

        bottom_frame = tk.Frame(self.top, height=frame_height, width=frame_width, bg='gray26')
        bottom_frame.pack(side='bottom')

    def render2D(self):
        """" Function to render the graph and assign it to the frame """
        """" As of right now, this is a test function to see if we can render the matplotlib on a Tkinter Frame """
        arr = self.read_data("MF_AE3.txt")
        grid = np.transpose(arr)
        fig = plt.imshow(grid, clim=(1e4, 1e6), origin="lower")
        plt.colorbar()

        canvas = FigureCanvasTkAgg(fig.figure, master=self.top)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # TODO: Insert code to render graph
        # Should be done by calling a controller
        # ...

        print("Rendered 2D graph")

    def read_data(self, filename):
        data = []
        with open(filename) as sourcefile:
            for line in sourcefile:
                row = [float(val) for val in line.split(", ") if val.strip()]
                data.append(row)
        arr = np.array(data, dtype=np.float64)
        return arr
