class ChronometerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_chronometer(self):
        self.model.start()
        self.view.display_start_button()

    def stop_chronometer(self):
        self.model.stop()
        self.view.display_stop_button()
        self.view.display_time(self.model.elapsed_time)

    def reset_chronometer(self):
        self.model.reset()
        self.view.display_reset_button()

    def update_chronometer(self):
        self.view.display_time(self.model.get_elapsed_time())
    
    def is_running_chronometer(self):
        return self.model.is_running()