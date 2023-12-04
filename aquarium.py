class Aquarium:
    def __init__(self, capacity):
        self._capacity = capacity  # Protected attribute
        self._tank_list = []  # Protected attribute, a list to store Tank objects

    def add_tank(self, tank):
        if len(self._tank_list) < self._capacity:
            self._tank_list.append(tank)

    def remove_tank(self, tank):
        if tank in self._tank_list:
            self._tank_list.remove(tank)

    def get_tank_list(self):
        return self._tank_list