#
# file: migrations/0002_create_table_product_item.py
#
from yoyo import step

__depends__ = {}

steps = [
  step(
      "CREATE TABLE ProductItem (product_id INT NOT NULL, item_id INT NOT NULL, FOREIGN KEY (product_id) REFERENCES Product (product_id), FOREIGN KEY (item_id) REFERENCES Item (item_id))"
  )
]
