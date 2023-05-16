

class DigitalClockDisplay:

    def __init__(self, hour, minute):

        self._hour_limit = 12
        self._hour = hour

        self._minute_limit = 60
        self._minute = minute

    def display(self):
        return f"{self._hour}:{self._minute}"

    def time_tick(self):

        self._hour += (self._minute + 1) // self._minute_limit
        self._hour = self._hour % self._hour_limit
        
        self._minute = (self._minute + 1) % self._minute_limit


    def set_minute(self, minute):
        if 0 <= minute and minute < self._minute_limit:
            self._minute = minute

    def set_hour(self, hour):
        if 0 < hour and hour < self._hour_limit:
            self._hour = hour

    def set_time(self, hour, minute):
        self.set_hour(hour)
        self.set_minute(minute)
            
