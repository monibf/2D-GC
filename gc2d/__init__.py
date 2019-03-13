import Tkinter
import tkMessageBox

top = Tkinter.Tk()
graphCanvas = Tkinter.Canvas(top, width=640, height=480, bg='darkgrey')


def render2D():
    graphCanvas.configure(bg='grey')

    # TODO: Insert code to generate the graph

    # ...

    print("Rendered 2D graph")

def initialize_mainframe():
    # Initialize mainframe

    # Initialize widgets
    graphCanvas.pack()

    render_button = Tkinter.Button(top, text ="Generate 2D", command =render2D)
    render_button.pack()
    top.mainloop()


initialize_mainframe()
