from Aquarium import Aquarium
from Fish import Tang, Kong, Clownfish


def printPretty(text):
    print()
    print(text)
    print("=" * len(text))
    print()


if __name__ == "__main__":
    printPretty("Adding four little fishes...")
    aq = Aquarium()
    aq.addFish(Tang("Lory", 10, "blue", False))
    aq.addFish([Clownfish("Serge", 5, "white", "green")])
    aq.addFish([Clownfish("Tibald", 11, "blue", "green"), Kong("Georgie", 10, "red")])
    aq.getStatus()

    printPretty("Feed those little fishes...")
    aq.feed()

    printPretty("Now let's remove the fat ones...")
    aq.removeFish()
    aq.getStatus()
