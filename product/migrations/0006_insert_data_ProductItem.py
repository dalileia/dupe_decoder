#
# file: migrations/0002_create_table_product_item.py
#
from yoyo import step

__depends__ = {}

steps = [
  step(
        "INSERT INTO ProductItem (product_id, item_id) VALUES (1,1),(1,2),(2,1),(2,3),(3,2)")
]



