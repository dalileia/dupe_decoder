from yoyo import step
step(
    "CREATE TABLE BrandProduct (brand_id INT NOT NULL, product_id INT NOT NULL, FOREIGN KEY (brand_id) REFERENCES Brand (brand_id), FOREIGN KEY (product_id) REFERENCES Product (product_id))",
    "DROP TABLE BrandProduct",
)