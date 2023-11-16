class Bot:
    def __init__(self):
        self.values = []
        self.low_to = None
        self.high_to = None

    def add_value(self, value):
        if len(self.values) <= 1:
            self.values.append(value)
            self.values.sort()

    def has_two_values(self):
        return len(self.values) == 2

    def give_values(self):
        low_value, high_value = self.values
        self.values = []
        return low_value, high_value
