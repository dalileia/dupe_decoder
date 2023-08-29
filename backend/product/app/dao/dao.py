from app.model.brand_data import BrandData
import pymysql.cursors
from app.dao.db import db_connection
import json
from app.model.item_data import ItemData
from app.model.product_data import ProductData


class Dao():

    def add_items(self,data):
        items = []  
        for item in data:
            id = item["id"]
            name = item["name"]
            item_temp = ItemData(id, name)
            items.append(item_temp)
        return items

    def return_all_products(self):
        mydb = db_connection()
        cursor = mydb.cursor(pymysql.cursors.DictCursor)
        sql = ('''SELECT JSON_OBJECT (
                                "id", p.product_id,
                                "name", p.product_name,
                                "items", IFNULL((
                                SELECT JSON_ARRAYAGG(JSON_OBJECT (
                                        "id", i.item_id,
                                        "name", i.item_name
                                    ))
                                    FROM Item i
                                    JOIN ProductItem pi ON pi.item_id = i.item_id
                                    WHERE p.product_id = pi.product_id
                                ), JSON_ARRAY())
                            ) Product
                            FROM Product p ''')
        cursor.execute(sql)
        data = cursor.fetchall()
        product_data = []  
        for product in data:
            obj = (product["Product"])
            product_obj = json.loads(obj)
            id = product_obj["id"]
            name = product_obj["name"]
            items = []
            product_temp = ProductData(id,name,items) 
            items = self.add_items(product_obj["items"])
            for item in items:
                item_temp = ItemData(item.id, item.name)
                product_temp.items.append(item_temp)
            product_data.append(product_temp)
        mydb.close()
        return product_data

    def return_one_product(self, id):
        mydb = db_connection()
        cursor = mydb.cursor(pymysql.cursors.DictCursor)
        sql = ('''SELECT JSON_OBJECT(
                "id", p.product_id,
                "name", p.product_name,
                "items", IFNULL(
                    (SELECT JSON_ARRAYAGG(
                        JSON_OBJECT(
                            "id", i.item_id,
                            "name", i.item_name
                        )
                    )
                    FROM Item i
                    JOIN ProductItem pi ON pi.item_id = i.item_id
                    WHERE p.product_id = pi.product_id
                    ), JSON_ARRAY())
            ) AS Product
            FROM Product p
            WHERE p.product_id=%s''')
        cursor.execute(sql%id)
        data = cursor.fetchone()
        product = json.loads(data["Product"])
        id = product["id"]
        name = product["name"]
        items = []
        product_data = ProductData(id,name,items) 
        items = self.add_items(product["items"])
        for item in items:
             item_temp = ItemData(item.id, item.name)
             product_data.items.append(item_temp)
        mydb.close()
        return product_data
    
    def return_all_brands(self):
        mydb = db_connection()
        cursor = mydb.cursor(pymysql.cursors.DictCursor)
        sql = ('''SELECT JSON_OBJECT (
                                "id", b.brand_id,
                                "name", b.brand_name,
                                "products", IFNULL((
                                SELECT JSON_ARRAYAGG(JSON_OBJECT (
                                        "id", p.product_id,
                                        "name", p.product_name
                                        ))
                                        FROM Product p
                                        JOIN BrandProduct bp ON bp.product_id = p.product_id
                                        WHERE b.brand_id = bp.brand_id
                                    ), JSON_ARRAY())
                                ) Brand 
                                FROM Brand b''')
        cursor.execute(sql)
        data = cursor.fetchall()
        brand_list = []
        for row in data:
            brand = json.loads(row['Brand'])
            id = brand['id']
            name = brand['name']
            products = brand['products']
            brand = BrandData(id,name,products)
            brand_list.append(brand)
        mydb.close()
        return brand_list

    def return_one_brand(self, id):
        mydb = db_connection()
        cursor = mydb.cursor(pymysql.cursors.DictCursor)
        sql = ('''SELECT JSON_OBJECT (
                                "id", b.brand_id,
                                "name", b.brand_name,
                                "products", IFNULL((
                                SELECT JSON_ARRAYAGG(JSON_OBJECT (
                                        "id", p.product_id,
                                        "name", p.product_name
                                        ))
                                        FROM Product p
                                        JOIN BrandProduct bp ON bp.product_id = p.product_id
                                        WHERE b.brand_id = bp.brand_id
                                    ), JSON_ARRAY())
                                ) Brand
                                FROM Brand b WHERE b.brand_id=%s''')
        cursor.execute(sql%id)
        data = cursor.fetchone()
        brand = json.loads(data['Brand'])
        id = brand['id']
        name = brand['name']
        products = brand['products']
        brand = BrandData(id,name,products)
        mydb.commit()
        return brand


    def return_one_item(self, id):
        mydb = db_connection()
        cursor = mydb.cursor(pymysql.cursors.DictCursor)
        sql = ('''SELECT JSON_OBJECT(
                "id", i.item_id ,
                "name", i.item_name ,
                "name_pt", i.item_name_pt,
                "description", i.item_description,
                "function", i.item_function
            ) AS Item
            FROM Item i 
            WHERE i.item_id=%s''')
        cursor.execute(sql%id)
        data = cursor.fetchone()
        item = json.loads(data['Item'])
        id = item['id']
        name = item['name']
        name_pt = item['name_pt']
        description = item['description']
        function = item['function']
        item = ItemData(id,name,name_pt,description,function)
        mydb.close()
        return item