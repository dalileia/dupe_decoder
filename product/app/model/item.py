
from app.model.item_data import ItemData

class Item():
    
    def __init__(self):
        pass
    
    def hydrate(self, data):
        self.id = data.id
        self.name = data.name
        
    def dehydrate(self):
        item = ItemData(self.id, self.name)
        return item
        
        
