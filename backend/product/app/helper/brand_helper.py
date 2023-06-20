from app.dao.dao import Dao
from app.model.brand import BrandData


class BrandHelper():

    @staticmethod
    def brand_product_id_list():
        brands = Dao().return_all_brands()
        print(brands)
        brand_product_id = {}
        for row in brands:
            brand_id = row['id']
            products = row['products']
            for product in products:
                product_id = product['id']
                print(brand_id,product_id)
                brand_product_id.update(brand_id[product_id])
        return brand_product_id