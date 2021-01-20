from typing import List
from Fish import Fish


class Aquarium:

    def __init__(self, fishes=None):
        if isinstance(fishes, list):
            self.fishes = fishes
        elif isinstance(fishes, type(None)):
            self.fishes = []
        elif isinstance(fishes, Fish) or isinstance(fishes.super(), Fish):
            self.fishes = [fishes]

    def addFish(self, fishes):
        if isinstance(fishes, List):
            self.fishes.extend(fishes)
        elif isinstance(fishes, Fish) or isinstance(fishes.super(), Fish):
            self.fishes.append(fishes)

    def feed(self):
        for fish in self.fishes:
            fish.feed()

    def removeFish(self):
        # removing on the fly would change the length of the list, hence we first find what to remove and then remove them in the second loop
        removable = []
        for i in range(len(self.fishes)):
            if self.fishes[i].weight >= 11:
                removable.append(self.fishes[i])

        for fish in removable:
            self.fishes.remove(fish)

    def getStatus(self):
        text = ""
        for fish in self.fishes:
            text += fish.status()
            print(fish.status())
        return text
