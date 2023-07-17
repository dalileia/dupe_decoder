from yoyo import step
step(
    "CREATE TABLE Item (item_id INT auto_increment NOT NULL, item_name VARCHAR(250),item_name_pt VARCHAR(250), item_description VARCHAR(5000), item_function VARCHAR(250), PRIMARY KEY (item_id))",
    "DROP TABLE Item",
)