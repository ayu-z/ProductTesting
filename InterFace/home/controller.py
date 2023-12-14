class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_home_interface(self):
        # Example: Update the DeviceInfoCard with a model name
        model_name = "Example Model"
        self.view.DeviceInfoCard.deviceNameupdate(model_name)
        # You can add more updates for other components as needed.