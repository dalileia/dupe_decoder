import unittest
from app.dao.dao import Dao
from app.model.product_data import ProductData

class TestReturnAllProducts(unittest.TestCase):
    """
    Test the return_all_products function from the dao 
    """

    def test_return_products_list(self):
        """
        Test that the returned list is not empty
        """
        result = len(Dao().return_all_products())
        self.assertNotEqual(result, 0)

    def test_check_instance(self):
        """
        Test that the instance of return is correct
        """
        result = Dao().return_all_products()[2]
        self.assertIsInstance(result, ProductData)
        
    def test_check_id_type(self):
        """
        Test that the type of id is int
        """
        product = Dao().return_all_products()[2]
        result = (product.id)
        self.assertIsInstance(result, int)


class TestReturnOneProduct(unittest.TestCase):
    """
    Test the return_all_products function from the dao 
    """

    def test_return_one_product(self):
        """
        Test that the returned list is not empty
        """
        result = len({Dao().return_one_product(1)})
        self.assertNotEqual(result, 0)

    def test_check_instance(self):
        """
        Test that the instance of return is correct
        """
        result = Dao().return_one_product(1)
        self.assertIsInstance(result, ProductData)
        
    def test_check_id_type(self):
        """
        Test that the type of id is int
        """
        product = Dao().return_one_products(1)
        result = (product.id)
        self.assertIsInstance(result, int)

        

if __name__ == '__main__':
    unittest.main()