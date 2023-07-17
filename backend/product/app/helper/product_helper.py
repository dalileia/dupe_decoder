
from app.dao.dao import Dao
from app.model.product import Product
from app.helper.brand_helper import BrandHelper


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
        brands = BrandHelper().brand_product_id_list()
        result = []
        brand_cache = []
        final_result = []
        for product in product_list:
            if product.id != product_main.id:
               comparison = product_main.compare(product)
               if comparison.percentage > 0.3:
                   result.append(comparison)
        sorted_result = sorted(result, key=lambda x: x.percentage, reverse=True)
        brand = brands.get(product_main.id)
        brand_cache.append(brand)
        for product in sorted_result:
            brand = brands.get(product.product.id)
            if brand not in brand_cache:
                final_result.append(product)
                brand_cache.append(brand)
        return final_result