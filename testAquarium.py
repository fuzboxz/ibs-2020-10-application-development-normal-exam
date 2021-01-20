import unittest
from Aquarium import Aquarium
from Fish import Tang, Clownfish


class AquariumTest(unittest.TestCase):

    def testInit(self):
        # single element in list
        aq = Aquarium([Tang("test", 1, 'red', False)])
        self.assertEqual(len(aq.fishes), 1)
        self.assertIsInstance(aq.fishes[0], Tang)

        # multiple elements in list
        aq = Aquarium([Tang("test", 1, 'red', False), Clownfish("test", 1, 'red', 'blue')])
        self.assertEqual(len(aq.fishes), 2)
        self.assertIsInstance(aq.fishes[1], Clownfish)

        # empty list
        aq = Aquarium()
        self.assertEqual(aq.fishes, [])

    def testAdd(self):
        # add single fish to tank
        aq = Aquarium()
        self.assertEqual(aq.fishes, [])
        aq.addFish(Tang("test", 1, 'red', False))
        self.assertEqual(len(aq.fishes), 1)
        self.assertIsInstance(aq.fishes[0], Tang)

        # add list of fishes to tank
        aq = Aquarium()
        self.assertEqual(aq.fishes, [])
        aq.addFish([Tang("test", 1, 'red', False)])
        self.assertEqual(len(aq.fishes), 1)
        self.assertIsInstance(aq.fishes[0], Tang)

        # add list with multiple elements to tank
        aq = Aquarium()
        self.assertEqual(aq.fishes, [])
        aq.addFish([Tang("test", 1, 'red', False), Clownfish("test", 1, 'red', 'blue')])
        self.assertEqual(len(aq.fishes), 2)
        self.assertIsInstance(aq.fishes[1], Clownfish)

        # add multiple elements to a list with existing elements
        aq = Aquarium(Tang("test", 1, 'red', False))
        aq.addFish([Tang("test", 1, 'red', False), Clownfish("test", 1, 'red', 'blue')])
        self.assertEqual(len(aq.fishes), 3)

    def testfeed(self):
        aq = Aquarium([Tang("test", 1, 'red', False)])
        aq.feed()
        self.assertEqual(len(aq.fishes), 1)
        self.assertIsInstance(aq.fishes[0], Tang)
        self.assertEqual(aq.fishes[0].weight, 2)

    def testremoveFish(self):
        # under 11
        aq = Aquarium([Tang("test", 10, 'red', False)])
        self.assertEqual(len(aq.fishes), 1)
        aq.removeFish()
        self.assertEqual(len(aq.fishes), 1)

        # 11
        aq = Aquarium([Tang("test", 11, 'red', False)])
        aq.removeFish()
        self.assertEqual(len(aq.fishes), 0)

        # above 11
        aq = Aquarium([Tang("test", 12, 'red', False)])
        self.assertEqual(len(aq.fishes), 1)
        aq.removeFish()
        self.assertEqual(len(aq.fishes), 0)

    def testgetstatus(self):
        # single element
        aq = Aquarium([Tang("test", 12, 'red', False)])
        self.assertEqual(aq.getStatus(), "test, weight: 12, color: red, short-term memory loss: false")

        # empty list
        aq = Aquarium()
        self.assertEqual(aq.getStatus(), '')

        # two lists
        aq = Aquarium([Tang("test", 1, 'red', False), Clownfish("test", 1, 'red', 'blue')])
        self.assertEqual(aq.getStatus(), "test, weight: 1, color: red, short-term memory loss: falsetest, weight: 1, color: red, stripes: blue")


if __name__ == "__main__":
    unittest.main()
