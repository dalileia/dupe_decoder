
from app.dao.dao import Dao
from app.model.compared_product import ComparedProduct
from app.model.item_data import ItemData
from app.model.product_data import ProductData
from app.model.item import Item
from app.helper.array_helper import ArrayHelper


class Product():
    
    def __init__(self):
        pass

    def hydrate(self, data):
        self.id = data.id
        self.name = data.name
        self.items = []
        for item_data in data.items:
            item = Item()
            item.hydrate(item_data)
            self.items.append(item)
        
    def dehydrate(self):
        product = ProductData(self.id, self.name, [])
        for item in self.items:
            item_data = ItemData(item.id, item.name)
            product.items.append(item_data)
        return product
    
    def identifies_equal_ids(self, product):
        self_items_ids = []
        product_items_ids = []
        for item in self.items:
            self_items_ids.append(item.id)
        for item in product.items:
            product_items_ids.append(item.id)
        result = ArrayHelper().identifies_equal_rows(self_items_ids,product_items_ids)
        return result

    def identifies_equal_items(self, product):
        equal_ids = self.identifies_equal_ids(product)
        items = []  
        for item in self.items:
            for id in equal_ids:
                if id == item.id:
                    items.append(item)
        return items        
    
    def identifies_different_ids(self, product):
        self_items_ids = []
        product_items_ids = []
        for item in self.items:
            self_items_ids.append(item.id)
        for item in product.items:
            product_items_ids.append(item.id)
        result = ArrayHelper().identifies_different_rows(self_items_ids,product_items_ids)
        return result    
        
    def identifies_different_items(self, product):
        equal_ids = self.identifies_different_ids(product)
        items = []  
        for item in self.items:
            for id in equal_ids:
                if id == item.id:
                    items.append(item)
        return items 

    def compare(self, product):
        equal_items = len(self.identifies_equal_items(product))
        different_items_main = len(self.identifies_equal_items(product))
        different_items_compared = len(product.identifies_different_items(self))
        percentage = 0 if self.items == 0 else equal_items/(equal_items + different_items_main + different_items_compared)
        compared_product = ComparedProduct(product,percentage)
        return compared_product


