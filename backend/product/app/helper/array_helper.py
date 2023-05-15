class ArrayHelper():
    
    @staticmethod
    def identifies_equal_rows(array_1,array_2):
        result = []
        result = set(array_1) & set(array_2)
        return result
    
    @staticmethod
    def identifies_different_rows(array_1,array_2):
        result = []
        result = set(array_1) - set(array_2)
        return result
