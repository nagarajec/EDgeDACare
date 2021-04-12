class DACareConfig:
    def __init__(self, second_counter=600, is_started=False, area_list=None, snooze_count=0):
        if area_list is None:
            area_list = []

        self._second_counter = second_counter
        self._snooze_count = snooze_count
        self._is_started = is_started
        self._area_list = area_list
        self._option_map = {
            "Eyes": {},
            "Lower Body": {
                "videos": ["leg", "lower_back", "waist"],
                "gifs": ["rear-pulses", "chair-squat", "calf-raise"]},
            "Neck": {},
            "Upper Body": {
                "videos": ["upper_back", "arm"],
                "gifs": ["chair-squat"]},
            "Shoulder": {}}

    # getter method for snooze count
    def get_snooze_count(self):
        return self._snooze_count

    # setter method for snooze count
    def set_snooze_count(self, count):
        self._snooze_count = count

    # getter method for second counter
    def get_second_counter(self, millisecond=False):
        return self._second_counter * 1000 if millisecond else self._second_counter

    # setter method for second counter
    def set_second_counter(self, count):
        self._second_counter = count

    # getter method for started
    def get_is_started(self):
        return self._is_started

    # setter method for started
    def set_is_started(self, is_started):
        self._is_started = is_started

    def get_option_map(self):
        return self._option_map

    def set_option_map(self, option_list):
        self._option_map = option_list

    def get_area_list(self):
        return self._area_list

    def set_area_list(self, area_list):
        self._area_list = area_list
