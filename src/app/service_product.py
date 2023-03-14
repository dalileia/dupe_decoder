from flask import jsonify, make_response
from flask_restful import Resource
import json
from app.dao.dao import Dao
from app.model.product import Product
from app.helper.json_object_helper import Object
from app.helper.product_helper import ProductHelper
from app.model.compared_product_list import ComparedProductList


class GetAllProducts(Resource):
    def get(self):
        products = None
        try:
            result_to_json = Object()
            result_to_json.products = Dao().return_all_products()
            result = result_to_json.toJSON()
            products = json.loads(result)
        except:
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
                result_to_json = Object()
                result_to_json.product = Dao().return_one_product(id)
                result = result_to_json.toJSON()
                product = json.loads(result)
            except:
                product = None
            return product
    

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
                result_to_json = Object()
                result_to_json.compared_product_list = ComparedProductList(product,result)
                result = result_to_json.toJSON()
                compared_products = json.loads(result)
            except:
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
            result_to_json = Object()
            result_to_json.products = result
            result = result_to_json.toJSON()
            searched_products = json.loads(result)          
        except:
            searched_products = None
        return searched_products







