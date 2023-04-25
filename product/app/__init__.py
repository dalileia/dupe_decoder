from flask import Flask
from flask_restful import Api

from app.service_product import GetAllProducts, GetOneProduct, CompareProducts, SearchProducts

app = Flask(__name__)
api = Api(app)


api.add_resource(GetAllProducts, '/products')
api.add_resource(GetOneProduct, '/products/<int:id>')
api.add_resource(CompareProducts, '/compare_products/<int:id>')
api.add_resource(SearchProducts, '/search_products/<string:searched>')
