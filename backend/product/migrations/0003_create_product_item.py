from yoyo import step
step(
    "CREATE TABLE ProductItem (product_id INT NOT NULL, item_id INT NOT NULL, FOREIGN KEY (product_id) REFERENCES Product (product_id), FOREIGN KEY (item_id) REFERENCES Item (item_id))",
    "DROP TABLE ProductItem",
)