class Observable:

    def __init__(self):
        """
        An Observable object can have observers added and removed from it that can be notified when required.
        """
        self.__observers = dict()

    def add_observer(self, observer, notify):
        """
        Adds an observer and its notify function to the Observable object
        :param observer: the observing object
        :param notify: the function to notify the observer with
        :return: None
        """
        if observer not in self.__observers:
            self.__observers[observer] = notify

    def remove_observer(self, observer):
        """
        :param observer: The observer to remove
        :return: None
        """
        if observer in self.__observers:
            self.__observers.pop(observer)

    def notify(self):
        """
        Notify all the observers.
        :return: None
        """
        for x in self.__observers:
            self.__observers[x]()
