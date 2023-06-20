CREATE TABLE Product (product_id INT auto_increment NOT NULL, product_name VARCHAR(250), PRIMARY KEY (product_id));
CREATE TABLE Item (item_id INT auto_increment NOT NULL, item_name VARCHAR(250),item_name_pt VARCHAR(250), item_description VARCHAR(5000), item_function VARCHAR(250), PRIMARY KEY (item_id));
CREATE TABLE ProductItem (product_id INT NOT NULL, item_id INT NOT NULL, FOREIGN KEY (product_id) REFERENCES Product (product_id), FOREIGN KEY (item_id) REFERENCES Item (item_id))
CREATE TABLE Brand (brand_id INT auto_increment NOT NULL, brand_name VARCHAR(250), PRIMARY KEY (brand_id));
CREATE TABLE BrandProduct (brand_id INT NOT NULL, product_id INT NOT NULL, FOREIGN KEY (brand_id) REFERENCES Brand (brand_id), FOREIGN KEY (product_id) REFERENCES Product (product_id))


