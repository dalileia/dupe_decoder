#
# file: migrations/0002_create_table_item.py
#
from yoyo import step

__depends__ = {}

steps = [
  step(
      "CREATE TABLE Item (item_id INT, item_name VARCHAR(20), PRIMARY KEY (item_id))"
  )
]
