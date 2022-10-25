import unittest
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):

    def setUp(self): 
      self.coffee_shop = CoffeeShop("The Prancing Pony", 100.00) 

    def test_coffee_shop_has_name(self): 
        self.assertEqual("The Prancing Pony", self.coffee_shop.name) 
    
    def test_increase_till(self):
        self.coffee_shop.increase_till(50)
        self.assertEqual(150, self.coffee_shop.till)
