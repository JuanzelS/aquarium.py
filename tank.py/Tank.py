class Tank:
    def __init__(self, capacity):
        self._capacity = capacity  # Protected attribute
        self._fish_list = []  # Protected attribute, a list to store Fish objects

    def add_fish(self, fish):
        if len(self._fish_list) < self._capacity:
            self._fish_list.append(fish)

    def remove_fish(self, fish):
        if fish in self._fish_list:
            self._fish_list.remove(fish)

    def get_fish_list(self):
        return self._fish_list
    