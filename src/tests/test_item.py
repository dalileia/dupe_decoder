import sys
sys.path.append('/home/dali/python_projects/compare_products/src/app/entity')
import sys
import unittest
from item_data import ItemData
from item import Item

class TesteItemClass(unittest.TestCase):
    """
    Test the item class and functions 
    """

    def test_hydreate_function(self):
        """
        Test if the hydrate function create an instance of Item
        """
        item_data = ItemData(1,"Item one")
        result = Item()
        result.hydrate(item_data)
        self.assertIsInstance(result, Item)
        
    def test_dehydrate_function(self):
        """
        Test if the function dehydrate return an instance of ItemData
        """
        item_data = ItemData(1,"Item one")
        item = Item()
        item.hydrate(item_data)
        result = item.dehydrate()
        self.assertIsInstance(result, ItemData)

        
if __name__ == '__main__':
    unittest.main()