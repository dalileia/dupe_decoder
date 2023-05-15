from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from app.service_product import GetAllProducts, GetOneProduct, CompareProducts, SearchProducts

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

api.add_resource(GetAllProducts, '/api/products')
api.add_resource(GetOneProduct, '/api/products/<int:id>')
api.add_resource(CompareProducts, '/api/products/compareProduct/<int:id>')
api.add_resource(SearchProducts, '/api/products/searchProducts/<string:searched>')
