class Config:
    def __init__(self, count=0, is_started=False, option_list=['Eye', 'Lower Body', 'Upper Body', 'Neck', 'Shoulder']):
        self._count = count
        self._is_started = is_started
        self._option_list = option_list

    # getter method for count
    def get_count(self):
        return self._count

    # setter method for count
    def set_count(self, count):
        self._count = count

    # getter method for started
    def get_is_started(self):
        return self._is_started

    # setter method for started
    def set_is_started(self, is_started):
        self._is_started = is_started

    def get_option_list(self):
        return self._option_list

    def set_option_list(self, option_list):
        self._option_list = option_list
