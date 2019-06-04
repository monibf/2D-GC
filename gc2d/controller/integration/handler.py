

class Handler():

    def __init__(self, model_wrapper):
        """
        Handler handles all model interaction with integration values 
        :param model_wrapper: the model to interact with
        """
        self.model_wrapper = model_wrapper
    
    def clear_value(self, key):
        """
        Removes an integration from the model wrapper
        :param key: the identifier of the integration that should be removed
        :return: None
        """
        self.model_wrapper.clear_integration(key)
    
    def change_label(self, key, new_label):
        """
        Takes an edited label and saves this to the appropriate Integration object in the model_wrapper
        :param key: the identifier of the integration to be changed
        :param new_label: a string of a new label
        :return: None
        """
        self.model_wrapper.update_integration(key, label=new_label)

    def show(self, key):
        """
        Toggle whether an integration is highlighted in 3D view
        :param key: the key of the integration to be toggled
        :return: None
        """
        self.model_wrapper.set_show(key, True)
    
    def hide(self, key):
        """
        Toggle whether an integration is highlighted in 3D view
        :param key: the key of the integration to be toggled
        :return: None
        """
        self.model_wrapper.set_show(key, False)