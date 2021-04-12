class Config:
    def __init__(self, count=0, is_started=False, option_list=None, area=''):
        self._count = count
        self._is_started = is_started
        self._option_list = option_list
        self._area = area
        self._option_list = ['Upper Back', 'Lower Back', 'Arm', 'Neck', 'Eyes', ]

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

    def get_area(self):
        return self._area

    def set_area(self, area):
        self._area = area
