
from app.model.brand_data import BrandData

class Brand():
    
    def __init__(self):
        pass
    
    def hydrate(self, data):
        self.id = data.id
        self.name = data.name
        self.products = data.products
        
    def dehydrate(self):
        brand = BrandData(self.id, self.name,self.products)
        return brand
        
        