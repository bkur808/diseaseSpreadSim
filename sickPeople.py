class People:
    def __init__(self, position):
        self.position = position
        self.state = 'Not Sick (Yet)'

    def infect(self):
        self.state = 'Sicko Mode'

    def recover(self):
        self.state = 'Over it and Immune'


