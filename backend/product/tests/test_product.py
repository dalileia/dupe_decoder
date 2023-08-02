import sys
import unittest
from app.model.item_data import ItemData
from app.model.item import Item
from app.model.product_data import ProductData
from app.model.product import Product

class TesteProductClass(unittest.TestCase):
    """
    Test the Product class and functions 
    """
    def test_hydrate_function(self):
        """
        Test if the hydrate function create an instance of Product
        """
        #arrange:
        item_1 = ItemData(1,"item one")
        item_2 = ItemData(2,"item two")
        product_data = ProductData(1,"product one",(item_1, item_2))
        result = Product()
        #act
        result.hydrate(product_data)
        #assert
        self.assertIsInstance(result, Product)
        
    def test_dehydrate_function(self):
        """
        Test if the function dehydrate return an instance of ProductData
        """
        #arrange
        item_1 = ItemData(1,"item one")
        item_2 = ItemData(2,"item two")
        product_data = ProductData(1,"product one",(item_1, item_2))
        product = Product()
        product.hydrate(product_data)
        #act
        result = product.dehydrate()
        #assert
        self.assertIsInstance(result, ProductData)
        self.assertIsInstance(result.items[0], ItemData)

    def test_identifies_equal_ids(self):
        """
        Test if the function identifies_equal_ids returns a list of equal numbers between two arrays    
        """
        #arrange
        item_1 = ItemData(1,"item one")
        item_2 = ItemData(2,"item two")
        item_3 = ItemData(3,"item three")
        product_data_1 = ProductData(1,"product one",(item_1, item_2))
        product_data_2 = ProductData(2,"product two",(item_2, item_3))
        product_1 = Product()
        product_1.hydrate(product_data_1)
        product_2 = Product()
        product_2.hydrate(product_data_2)
        #act
        result = product_1.identifies_equal_ids(product_2)
        expected = set([2])
        #assert
        self.assertEqual(expected, result)

    def test_identifies_equal_items(self):
        """
        Test if the function identifies_equal_items compare two arrays of Item objects and return a list of equal items
        """
        #arrange
        item_1 = ItemData(1,"item one")
        item_2 = ItemData(2,"item two")
        item_3 = ItemData(3,"item three")
        product_data_1 = ProductData(1,"product one",(item_1, item_2))
        product_data_2 = ProductData(2,"product two",(item_2, item_3))
        product_1 = Product()
        product_1.hydrate(product_data_1)
        product_2 = Product()
        product_2.hydrate(product_data_2)
        item_expected = Item()
        item_expected.hydrate(item_2)
        item_result = product_1.identifies_equal_items(product_2)[0]
        #act
        result = (item_result.id, item_result.name)
        expected = (item_expected.id, item_expected.name)
        #assert
        self.assertEqual(expected, result)

    def test_identifies_different_ids(self):
        """
        Test if the function identifies_diferent_ids returns a list of diferent numbers between two arrays    
        """
        #arrange
        item_1 = ItemData(1,"item one")
        item_2 = ItemData(2,"item two")
        item_3 = ItemData(3,"item three")
        product_data_1 = ProductData(1,"product one",[(item_1),(item_2)])
        product_data_2 = ProductData(2,"product two",[(item_2), (item_3)])
        product_1 = Product()
        product_1.hydrate(product_data_1)
        product_2 = Product()
        product_2.hydrate(product_data_2)
        #act
        result = product_1.identifies_different_ids(product_2)
        expected = set([1])
        #assert
        self.assertEqual(expected, result)

    def test_identifies_different_items(self):
        """
        Test if the function identifies_different_items compare two arrays of Item objects and return a list of different items
        """
        #arrange
        item_1 = ItemData(1,"item one")
        item_2 = ItemData(2,"item two")
        item_3 = ItemData(3,"item three")
        product_data_1 = ProductData(1,"product one",[(item_1),(item_2)])
        product_data_2 = ProductData(2,"product two",[(item_3)])
        product_1 = Product()
        product_1.hydrate(product_data_1)
        product_2 = Product()
        product_2.hydrate(product_data_2)
        item_expected = Item()
        item_expected.hydrate(item_1)
        item_result = product_1.identifies_different_items(product_2)[0]
        #act
        result = (item_result.id, item_result.name)
        expected = (item_expected.id, item_expected.name)
        #assert
        self.assertEqual(expected, result)      

if __name__ == '__main__':
    unittest.main()