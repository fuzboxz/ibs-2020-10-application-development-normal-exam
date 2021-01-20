import unittest
from unittest import TestCase
from Fish import Fish, Kong, Tang, Clownfish


class TestFish(TestCase):

    dory = Fish("Nemo", 9, "blue")

    def testInit(self):
        self.assertEqual(self.dory.name, "Nemo")
        self.assertEqual(self.dory.weight, 9)
        self.assertEqual(self.dory.color, "blue")


class TestKong(TestCase):

    def testInit(self):
        king = Kong("King", 5, "black")
        self.assertEqual(king.name, "King")
        self.assertEqual(king.weight, 5)
        self.assertEqual(king.color, "black")

    def testFeed(self):
        king = Kong("King", 5, "black")
        king.weight = 5
        king.feed()
        self.assertEqual(king.weight, 7)

    def testStatus(self):
        king = Kong("King", 5, "black")
        self.assertEqual(king.status(), 'King, weight: 5, color: black')


class TestTang(TestCase):

    def testInit(self):
        dory = Tang("Dory", 9, "blue", True)
        self.assertEqual(dory.name, "Dory")
        self.assertEqual(dory.weight, 9)
        self.assertEqual(dory.color, "blue")
        self.assertEqual(dory.stml, True)

    def testFeed(self):
        dory = Tang("Dory", 9, "blue", True)
        dory.feed()
        self.assertEqual(dory.weight, 10)

    def testStatus(self):
        dory = Tang("Dory", 9, "blue", True)
        self.assertEqual(dory.status(), 'Dory, weight: 9, color: blue, short-term memory loss: true')


class TestClownfish(TestCase):

    def testInit(self):
        it = Clownfish("It", 5, "white", "red")
        self.assertEqual(it.name, "It")
        self.assertEqual(it.weight, 5)
        self.assertEqual(it.color, "white")
        self.assertEqual(it.stripes, "red")

    def testFeed(self):
        it = Clownfish("It", 5, "white", "red")
        it.feed()
        self.assertEqual(it.weight, 6)

    def testStatus(self):
        it = Clownfish("It", 5, "white", "red")
        self.assertEqual(it.status(), 'It, weight: 5, color: white, stripes: red')


if __name__ == "__main__":
    unittest.main()
