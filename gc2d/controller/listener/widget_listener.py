class WidgetListener:

    def __init__(self, widget):
        """
        Overrides the mouse and keyboard events of Qt widgets. Seems to work on both Qt and PyQtGraph
        widgets.
        :param widget: The widget to override
        """
        self.widget = widget

        self.super_mouse_press_event = widget.mousePressEvent
        widget.mousePressEvent = self.mouse_press_event

        self.super_mouse_release_event = widget.mouseReleaseEvent
        widget.mouseReleaseEvent = self.mouse_release_event

        self.super_mouse_move_event = widget.mouseMoveEvent
        widget.mouseMoveEvent = self.mouse_move_event

        # self.super_mouse_clicked_event = plot.mouseClickedEvent  # Bugged for some reason.
        widget.mouseClickedEvent = self.mouse_clicked_event

        self.super_mouse_scroll_event = widget.wheelEvent
        widget.wheelEvent = self.mouse_scroll_event

        self.super_mouse_leave_event = widget.leaveEvent
        widget.leaveEvent = self.mouse_leave_event

        self.super_key_press_event = widget.keyPressEvent
        widget.keyPressEvent = self.key_press_event

        self.super_key_release_event = widget.keyReleaseEvent
        widget.keyReleaseEvent = self.key_release_event

    def mouse_press_event(self, event):
        """"
        Intercepts the mousePressEvent of the plot
        :param event: the mousePressEvent
        :return: None
        """
        self.super_mouse_press_event(event)

    def mouse_release_event(self, event):
        """
        Intercepts mouseReleaseEvent of the plot
        :param event: the mouseReleaseEvent
        :return: None
        """
        self.super_mouse_release_event(event)

    def mouse_clicked_event(self, event):
        """
        Intercepts mouseClickedEvent of the plot
        :param event: the mouseClickedEvent
        :return: None
        """
        # self.super_mouse_clicked_event(event)  # Bugged for some reason.
        pass

    def mouse_move_event(self, event):
        """
        Intercepts mouseMoveEvent of the plot
        :param event: the mouseMovedEvent
        :return: None
        """
        self.super_mouse_move_event(event)

    def mouse_scroll_event(self, event):
        """
        Intercepts mouseScrollEvent of the plot
        :param event: the mouseScrollEvent
        :return: None
        """
        self.super_mouse_scroll_event(event)

    def mouse_leave_event(self, event):
        """
        Intercepts leaveEvent of the QWidget
        :param event: the leave event
        :return: None
        """
        self.super_mouse_leave_event(event)

    def key_press_event(self, event):
        """
        Intercepts keyPressEvent of the plot
        :param event: the keyPressEvent
        :return: None
        """
        self.super_key_press_event(event)

    def key_release_event(self, event):
        """
        Intercepts keyReleaseEvent of the plot
        :param event: the keyReleaseEvent
        :return: None
        """
        self.super_key_release_event(event)
