
from app.dao.dao import Dao
from app.model.product import Product


class ProductHelper():
    
    @staticmethod
    def product_id_list():
        products = Dao().return_all_products()
        id_list = []
        for product in products:
            id_list.append(product.id)
        return id_list
    
    @staticmethod
    def product_list():
        product_data = Dao().return_all_products()
        product_list = []
        for product in product_data:
            product_temp = Product()
            product_temp.hydrate(product)
            product_list.append(product_temp)
        return product_list
    
    @staticmethod
    def compared_product_list(product_main, product_list):
        result = []
        
        for product in product_list:
            if product.id != product_main.id:
               comparison = product_main.compare(product)
               if comparison.percentage >0:
                   result.append(comparison)
        return result

# product_data_1 = Dao().return_one_product(1)
# product_list = ProductHelper.product_list()
# product_1 = Product()
# product_1.hydrate(product_data_1)


# result = ProductHelper.compared_product_list(product_1,product_list)
# for product in result:
#     print(product.percentage)
