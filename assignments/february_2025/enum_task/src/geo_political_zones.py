from enum import Enum

class GeoPoliticalZONES(Enum):

    def __init__(self, states):
        self._states = states

    NORTH_CENTRAL = ("Benue", "FCT", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateu")
    NORTH_EAST = ("Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe")
    NORTH_WEST = ("Kaduna", "Katsina", "Kano", "Kebbi", "Sokoto", "Jigawa", "Zamfara")
    SOUTH_EAST = ("Abia", "Anambra", "Ebonyi", "Enugu", "Imo")
    SOUTH_SOUTH = ("Akwa-Ibom", "Bayelsa", "Cross-River", "Delta", "Edo", "Rivers")
    SOUTH_WEST = ("Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo")

    def get_state(self, state):
        for zone in GeoPoliticalZONES:
            if state in zone:
                return True
        return False