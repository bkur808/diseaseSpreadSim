class Individual:
    def __init__(self, position):
        self.position = position
        self.state = 'Not Sick (Yet)'
        self.sickcounter = None
        self.lifestatus = 'Living'

    def infect(self):
        self.state = 'Sicko Mode'

    def recover(self):
        self.state = 'Over it and Immune'

    def reduceSickCount(self):
        self.sickcounter -= 1

    





