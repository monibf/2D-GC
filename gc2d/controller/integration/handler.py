

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

    def toggle_show(self, key):
        # still in progress
        self.model_wrapper.toggle_show(key)
