#
# file: migrations/0002_create_table_product_item.py
#
from yoyo import step

__depends__ = {}

steps = [
  step(
        '''INSERT INTO Product (product_id, product_name) VALUES (1, "Product one"),(2,"Product two"),(3,"Product three")''')
]



