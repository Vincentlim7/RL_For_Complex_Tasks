class Agent:

    def __init__(self):
        self.id = 0
        self.symbol = "I"
        self.action_list = ["North", "South", "East", "West"]
        self.position = None
        self.energy_init = 40
        self.energy = self.energy_init

    def get_id(self):
        return self.id

    def get_symbol(self):
        return self.symbol

    def set_position(self, new_position: tuple):
        self.position = new_position

    def get_position(self):
        return self.position

    def get_energy(self):
        return self.energy