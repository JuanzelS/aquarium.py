class Viewer:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age  # Protected attribute
        self._observed_tank = None  # Protected attribute, initially not observing any tank

    def observe_tank(self, tank):
        self._observed_tank = tank
        print(f"{self._name} is observing the fish in Tank {tank.get_tank_number()}.")

    def stop_observing(self):
        self._observed_tank = None
        print(f"{self._name} has stopped observing.")

    def get_observed_tank(self):
        return self._observed_tank