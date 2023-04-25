#
# file: migrations/0001_create_table_product.py
#
from yoyo import step

__depends__ = {}

steps = [
  step(
      "CREATE TABLE Product (product_id INT, product_name VARCHAR(20), PRIMARY KEY (product_id))"
  )
]
