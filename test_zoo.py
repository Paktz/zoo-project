import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_invalid_age(self): #C1b1
        self.assertEqual(self.zoo.get_ticket_price(-1),"negative age doesn't exist")

    def test_child_tickets(self): #C1b2
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        self.assertEqual(self.zoo.get_ticket_price(6), 50)
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_teen_tickets(self): #C1b3
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(16), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_adult_tickets(self): #C1b4
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(40), 150)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_senior_tickets(self): #C1b5
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
        self.assertEqual(self.zoo.get_ticket_price(100), 100)

if __name__ == '__main__':
    unittest.main()