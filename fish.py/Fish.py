class Fish:
    def __init__(self, species, color):
        self._species = species  # Protected attribute
        self._color = color  # Protected attribute
        self._is_alive = True  # Protected attribute, indicating whether the fish is alive

    def swim(self):
        print(f"The {self._color} {self._species} is swimming.")

    def feed(self):
        print(f"The {self._color} {self._species} is being fed.")

    def is_alive(self):
        return self._is_alive

    def set_alive_status(self, status):
        self._is_alive = status