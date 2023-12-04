class Caretaker:
    def __init__(self, name):
        self._name = name  # Protected attribute
        self._assigned_tank = None  # Protected attribute, initially not assigned

    def assign_tank(self, tank):
        self._assigned_tank = tank

    def clean_tank(self):
        if self._assigned_tank:
            print(f"{self._name} is cleaning the tank.")
            # Additional logic for tank cleaning can be added here
        else:
            print(f"{self._name} is not assigned to any tank.")

    def feed_fish_in_assigned_tank(self):
        if self._assigned_tank:
            fish_list = self._assigned_tank.get_fish_list()
            for fish in fish_list:
                fish.feed()
        else:
            print(f"{self._name} is not assigned to any tank.")