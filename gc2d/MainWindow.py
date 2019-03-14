import Tkinter


class MainWindow:
    """" The main window class. Creates and con the global components of the UI """
    top = Tkinter.Tk()

    def __init__(self):
        self.init_mainframe()

    def render2D(self):
        """" Function to render the graph and assign it to the frame """

        # TODO: Insert code to render graph
        # Should be done by calling a controller
        # ...

        print("Rendered 2D graph")

    def init_top_frame(self, frame_height, graph_width, sidebar_width):
        """" Initialize the top frame. This includes the graph and graph control frame """

        top_frame = Tkinter.Frame(self.top, height=frame_height, width=graph_width + sidebar_width, bg='gray')
        top_frame.pack(side='top')

        left_frame = Tkinter.Frame(top_frame, height=frame_height, width=sidebar_width, bg='darkgray')
        left_frame.pack(side='left')

        graph_frame = Tkinter.Frame(top_frame, height=frame_height, width=graph_width, bg='lightgray')
        graph_frame.pack(side='right')

    def init_bottom_frame(self, frame_height, frame_width):
        """" Initialize the top frame. This includes other controls """

        bottom_frame = Tkinter.Frame(self.top, height=frame_height, width=frame_width, bg='gray26')
        bottom_frame.pack(side='bottom')

    def init_mainframe(self):
        """ Initialize the main frame. This includes every UI element """

        top_height = 480
        bottom_height = 80

        graph_width = 640
        sidebar_width = 100

        self.init_top_frame(frame_height=top_height, graph_width=graph_width, sidebar_width=sidebar_width)
        self.init_bottom_frame(frame_height=bottom_height, frame_width=graph_width + sidebar_width)

        self.top.mainloop()
