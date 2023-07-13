from yoyo import step
step(
    "CREATE TABLE Product (product_id INT auto_increment NOT NULL, product_name VARCHAR(250), PRIMARY KEY (product_id))",
    "DROP TABLE Product",
)