class DACareConfig:
    def __init__(self, second_counter=3600, is_started=False, area_list=None):
        if area_list is None:
            area_list = []

        self._second_counter = second_counter
        self._is_started = is_started
        self._area_list = area_list
        self._option_map = {
            "Eyes": {},
            "Lower Body": {
                "movlee_video": ["leg", "lower_back", "waist"],
                "gifs": ["rear-pulses", "chair-squat", "calf-raise"]},
            "Neck": {},
            "Upper Body": {
                "movlee_video": ["upper_back", "arm"],
                "gifs": ["chair-squat"]},
            "Shoulder": {},
            "Waist": {}}

    # getter method for count
    def get_second_counter(self):
        return self._second_counter

    # setter method for count
    def set_second_counter(self, count):
        self._second_counter = count

    # getter method for started
    def get_is_started(self):
        return self._is_started

    # setter method for started
    def set_is_started(self, is_started):
        self._is_started = is_started

    def get_option_list(self):
        return self._option_map

    def set_option_list(self, option_list):
        self._option_map = option_list

    def get_area_list(self):
        return self._area_list

    def set_area_list(self, area_list):
        self._area_list = area_list
