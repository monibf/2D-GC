class PlotListener:

    def __init__(self, plot, model_wrapper):
        self.model_wrapper = model_wrapper

        plot.mousePressEvent = self.mouse_press_event
        plot.mouseReleaseEvent = self.mouse_release_event
        plot.mouseMoveEvent = self.mouse_move_event
        plot.mouseClickedEvent = self.mouse_clicked_event
        plot.wheelEvent = self.mouse_scroll_event
        plot.keyPressEvent = self.key_press_event
        plot.keyReleaseEvent = self.key_release_event

    def mouse_press_event(self, event):
        print("pressed")

    def mouse_release_event(self, event):
        print("released")

    def mouse_clicked_event(self, event):
        print("clicked")

    def mouse_move_event(self, event):
        print("moved")

    def mouse_scroll_event(self, event):
        print("scroll")

    def key_press_event(self, event):
        print("key_pressed")

    def key_release_event(self, event):
        print("key_released")
