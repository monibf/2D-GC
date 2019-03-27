
class Plot3DListener:

    def __init__(self, plot3d, model_wrapper):
        self.model_wrapper = model_wrapper

        plot3d.mousePressEvent = self.mouse_press_event
        plot3d.mouseReleaseEvent = self.mouse_release_event
        plot3d.mouseMoveEvent = self.mouse_move_event
        plot3d.mouseClickedEvent = self.mouse_clicked_event
        plot3d.wheelEvent = self.mouse_scroll_event
        plot3d.keyPressEvent = self.key_press_event
        plot3d.keyReleaseEvent = self.key_release_event

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

    def key_press_event(self, event):
        print("key_pressed")
        return

    def key_release_event(self, event):
        print("key_released")
        return
