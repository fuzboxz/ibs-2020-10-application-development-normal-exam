class Aquarium:

    def __init__(self, fishes=None):
        if fishes is not None:
            self.fishes = fishes
        else:
            self.fishes = []

    def addFish(self, fish):
        self.fishes.append(fish)
        return True

    def feed(self):
        for fish in self.fishes:
            fish.feed()

    def removeFish(self):
        for i in len(self.fishes):
            if self.fishes[i].weight <= 11:
                self.fishes.remove(self.fishes[i])

    def getStatus(self):
        for fish in self.fishes:
            print(fish.status())
