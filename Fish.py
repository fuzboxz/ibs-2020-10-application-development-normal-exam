from abc import abstractclassmethod


class Fish():

    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def status(self):
        return ', '.join([self.name, 'weight: ' + str(self.weight), 'color: ' + self.color])

    @abstractclassmethod
    def feed(self):
        return None


class Kong(Fish):

    def feed(self):
        self.weight += 2


class Clownfish(Fish):

    def __init__(self, name, weight, color, stripes):
        super().__init__(name, weight, color)
        self.stripes = stripes

    def feed(self):
        self.weight += 1

    def status(self):
        return ', '.join([super().status(), "stripes: " + self.stripes])


class Tang(Fish):

    def __init__(self, name, weight, color, stml):
        super().__init__(name, weight, color)
        self.stml = stml

    def feed(self):
        self.weight += 1

    def status(self):
        return ', '.join([super().status(), "short-term memory loss: " + str(self.stml).lower()])
