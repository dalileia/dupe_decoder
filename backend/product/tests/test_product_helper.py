import unittest
import sys
from app.helper.product_helper import ProductHelper
from app.dao.dao import Dao
from app.model.product import Product
from app.model.compared_product import ComparedProduct

class TesteProducIdList(unittest.TestCase):
    """
    Test the function product_id_list from ProductHelper class
    """

    def test_product_id_list(self):
        """
        Test if the product_id_list function return a list of product ids
        """
        #act
        result = len(ProductHelper().product_id_list())
        #assert
        self.assertNotEqual(result, 0)

class TesteProductList(unittest.TestCase):
    """
    Test the product_list function from the product helper class 
    """
    
    def test_product_list(self):
        """
        Test if the product id list function return a list of product ids
        """
        #act
        result = len(ProductHelper().product_list())
        #assert
        self.assertNotEqual(result, 0)
    
    def test_product_list_instance(self):
        """
        Test if the product_list function return a instance of Product
        """
        #act
        result = ProductHelper.product_list()[1]
        #assert
        self.assertIsInstance(result, Product)

class TesteCompareProductList(unittest.TestCase):
    """
    Test the product_list function from the product helper class 
    """
    
    def test_compare_product_list(self):
        """
        Test if the compare_product_list function return a list
        """
        #arrange
        product_list = ProductHelper().product_list()
        product_data = Dao().return_one_product(1)
        product = Product()
        product.hydrate(product_data)
        #act
        result = len(ProductHelper().compared_product_list(product,product_list))
        #assert
        self.assertNotEqual(result, 0)
    
    def test_compare_product_list_instance(self):
        """
        Test if the compare_product_list function return a instance of ComparedProduct
        """
        #arrange
        product_list = ProductHelper().product_list()
        product_data = Dao().return_one_product(1)
        product = Product()
        product.hydrate(product_data)
        #act
        result = ProductHelper().compared_product_list(product,product_list)[1]
        #assert
        self.assertIsInstance(result, ComparedProduct)
        
if __name__ == '__main__':
    unittest.main()