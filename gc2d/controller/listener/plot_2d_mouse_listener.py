
class Plot2DMouseListener:

    def __init__(self, plot2d, model_wrapper):
        self.model_wrapper = model_wrapper

        plot2d.mousePressEvent = self.mouse_press_event
        plot2d.mouseReleaseEvent = self.mouse_release_event
        plot2d.mouseMoveEvent = self.mouse_move_event
        plot2d.mouseClickedEvent = self.mouse_clicked_event
        plot2d.wheelEvent = self.mouse_scroll_event

    def mouse_press_event(self, event):
        print("pressed")
        return

    def mouse_release_event(self, event):
        print("released")
        return

    def mouse_clicked_event(self, event):
        print("clicked")
        return

    def mouse_move_event(self, event):
        print("moved")
        return

    def mouse_scroll_event(self, event):
        print("scroll")
        return
