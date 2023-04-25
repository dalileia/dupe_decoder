#
# file: migrations/0002_create_table_product_item.py
#
from yoyo import step

__depends__ = {}

steps = [
  step(
        '''INSERT INTO Item (item_id, item_name) VALUES (1, "Item one"),(2,"Item two"),(3,"Item three")''')
]



