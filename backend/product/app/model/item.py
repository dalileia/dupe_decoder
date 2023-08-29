
from app.model.item_data import ItemData

class Item():
    
    def __init__(self):
        pass
    
    def hydrate(self, data):
        self.id = data.id
        self.name = data.name
        self.name_pt = data.name_pt
        self.description = data.description
        self.function = data.function
        
    def dehydrate(self):
        item = ItemData(self.id, self.name, self.name_pt, self.description, self.function)
        return item
        
        
