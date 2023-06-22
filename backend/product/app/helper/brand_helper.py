from app.dao.dao import Dao
from app.model.brand import BrandData


class BrandHelper():

    @staticmethod
    def brand_product_id_list():
        brands = Dao().return_all_brands()
        brand_product = {}
        for brand in brands:
            brand_id = brand.id
            products = brand.products
            for product in products:
                product_id = product['id']
                brand_product[product_id] = brand_id
        return brand_product
    
    