from datetime import datetime, timedelta

class Chronometer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = timedelta()

    def start(self):
        self.start_time = datetime.now()

    def stop(self):
        if self.start_time:
            self.elapsed_time += datetime.now() - self.start_time
            self.start_time = None

    def reset(self):
        self.start_time = None
        self.elapsed_time = timedelta()

    def get_elapsed_time(self):
        if self.start_time:
            return self.elapsed_time + (datetime.now() - self.start_time)
        return self.elapsed_time
    
    def is_running(self):
        if self.start_time:
            return True
        return False

