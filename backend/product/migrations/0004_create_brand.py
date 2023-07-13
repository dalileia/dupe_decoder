from yoyo import step
step(
    "CREATE TABLE Brand (brand_id INT auto_increment NOT NULL, brand_name VARCHAR(250), PRIMARY KEY (brand_id))",
    "DROP TABLE Brand",
)