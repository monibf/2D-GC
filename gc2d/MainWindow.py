import Tkinter

class MainWindow:

    top = Tkinter.Tk()

    def __init__(self):
        self.init_mainframe()

    def render2D(self):
        # TODO: Insert code to render graph
        # Should be done by calling a controller
        # ...

        print("Rendered 2D graph")

    def init_top_frame(self):
        """" Initialize the top frame. This includes the graph and graph control frame """
        graph_width = 640
        graph_height = 480

        sidebar_width = 100

        top_frame = Tkinter.Frame(self.top, height=graph_height, width=graph_width + sidebar_width, bg='gray')
        top_frame.pack(side='top')

        left_frame = Tkinter.Frame(top_frame, height=graph_height, width=sidebar_width, bg='darkgray')
        left_frame.pack(side='left')

        graph_frame = Tkinter.Frame(top_frame, height=graph_height, width=graph_width, bg='lightgray')
        graph_frame.pack(side='right')

    def init_bottom_frame(self):
        """" Initialize the top frame. This includes other controls """

        bottom_frame = Tkinter.Frame(self.top, height=80, width=640 + 100, bg='gray26')
        bottom_frame.pack(side='bottom')

    def init_mainframe(self):
        """ Initialize the main frame. This includes every UI element """

        self.init_top_frame()
        self.init_bottom_frame()

        self.top.mainloop()
