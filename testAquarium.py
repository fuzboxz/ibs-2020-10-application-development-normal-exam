import unittest
from Aquarium import Aquarium
from Fish import Tang

class AquariumTest(unittest.TestCase):

    def testInit(self):
        aq = Aquarium([Tang("test", 1, 'red', False)])
        self.assertEqual(len(aq.fishes), 1)

    def testAdd():
        pass

    def testfeed():
        pass

    def testremoveFish():
        pass

    def testgetstatus():
        pass