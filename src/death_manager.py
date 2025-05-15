# src/death_manager.py

class DeathManager:
    def __init__(self):
        self.deaths = 0

    def player_died(self):
        self.deaths += 1

    def get_deaths(self):
        return self.deaths