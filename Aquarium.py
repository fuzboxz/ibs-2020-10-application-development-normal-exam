from typing import List
from Fish import Fish
from os import linesep

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
        for i in range(len(self.fishes)):
            if self.fishes[i].weight >= 11:
                self.fishes.remove(self.fishes[i])

    def getStatus(self):
        text = ""
        for fish in self.fishes:
            text += fish.status()
            print(fish.status())
        return text
