from flask import jsonify, make_response
from flask_restful import Resource
import json
from app.dao.dao import Dao
from app.model.product import Product
from app.helper.product_helper import ProductHelper
from app.model.compared_product_list import ComparedProductList


class GetAllProducts(Resource):
    def get(self):
        products = None
        try:
            result = Dao().return_all_products()
            products = json.dumps(result, default=lambda o: o.__dict__)
            products = json.loads(products)
        except Exception as e:
            print(e)
            products = None
        return products

class GetOneProduct(Resource):
    def get(self, id):
        product = None
        product_id_list = ProductHelper.product_id_list()
        if (id not in product_id_list):
            return make_response(jsonify({"error": "400"}), 400)
        else:
            try:
                product_data = Dao().return_one_product(id)
                product = json.dumps(product_data, default=lambda o: o.__dict__)
                product = json.loads(product)
            except Exception as e:
                print(e)
                product = None
            return product
        
class GetOneBrand(Resource):
    def get(self, id):
        brand = None
        try:
            brand_data = Dao().return_one_brand(id)
            brand = json.dumps(brand_data, default=lambda o: o.__dict__)
            brand = json.loads(brand)
        except Exception as e:
            print(e)
            brand = None
        return brand    
    
class GetAllBrands(Resource):
    def get(self):
        brand = None
        try:
            brand_data = Dao().return_all_brands()
            brand = json.dumps(brand_data, default=lambda o: o.__dict__)
            brand = json.loads(brand)
        except Exception as e:
            print(e)
            brand = None
        return brand

class CompareProducts(Resource):
    def get(self, id):
        compared_products = None
        product_id_list = ProductHelper.product_id_list()
        if (id not in product_id_list):
            return make_response(jsonify({"error": "400"}), 400)
        else:
            try:
                product_data = Dao().return_one_product(id)
                product_list = ProductHelper.product_list()
                product = Product()
                product.hydrate(product_data)
                result = ProductHelper.compared_product_list(product,product_list)
                result.sort(key=lambda x: x.percentage, reverse=True)
                compared_products = ComparedProductList(product,result)
                compared_products = json.dumps(compared_products, default=lambda o: o.__dict__)
                compared_products = json.loads(compared_products)
            except Exception as e:
                print(e)
                compared_products = None
            return compared_products
    
class SearchProducts(Resource):
    def get(self, searched):
        searched_products = None
        try:
            result = []
            product_list = ProductHelper.product_list() 
            for product in product_list:
                if(product.name.lower().find(searched) != -1): 
                    result.append(product)
            searched_products = json.dumps(result, default=lambda o: o.__dict__)
            searched_products = json.loads(searched_products)
        except Exception as e:
            print(e)
            searched_products = None
        return searched_products

class GetOneItem(Resource):
    def get(self, id):
        item = None
        try:
            item_data = Dao().return_one_item(id)
            item = json.dumps(item_data, default=lambda o: o.__dict__)
            item = json.loads(item)
        except Exception as e:
            print(e)
            item = None
        return item




