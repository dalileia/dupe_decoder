import unittest
import sys
sys.path.append('/home/dali/python_projects/compare_products/src')
from app.helper.array_helper import ArrayHelper


class TesteArrayHelperClass(unittest.TestCase):
    """
    Test the ArrayHelper functions 
    """

    def test_identifies_equal_rows(self):
        """
        Test if the identifies equal rows function return an array with equal items of an array
        """
        #arrange
        array_1 = [1,2,3,4]
        array_2 = [3,4,5,6]
        #act
        result = ArrayHelper().identifies_equal_rows(array_1, array_2)
        expected = set([3,4])
        #assert
        self.assertEqual(expected, result)
    
    def test_identifies_equal_rows_2(self):
        """
        Test if the identifies equal rows function return an array with equal items of an array
        """
        #arrange
        array_1 = [1,2]
        array_2 = [5,6]
        #act
        result = ArrayHelper().identifies_equal_rows(array_1, array_2)
        expected = set([])
        #assert
        self.assertEqual(expected, result)
    
    def test_identifies_different_rows(self):
        """
        Test if the identifies different rows function return an array with different items of an array
        """
        #arrange
        array_1 = [1,2,3,4]
        array_2 = [3,4,5,6]
        #act
        result = ArrayHelper().identifies_different_rows(array_1, array_2)
        expected = set([1,2])
        #assert
        self.assertEqual(expected, result)
        
    def test_identifies_different_rows_2(self):
        """
        Test if the identifies different rows function return an array with different items of an array
        """
        #arrange
        array_1 = [3,4]
        array_2 = [3,4]
        #act
        result = ArrayHelper().identifies_different_rows(array_1, array_2)
        expected = set([])
        #assert
        self.assertEqual(expected, result)
        
        
if __name__ == '__main__':
    unittest.main()