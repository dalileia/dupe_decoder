from flask import jsonify
import pymysql.cursors
from app.dao.db import mydb
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
                                    JOIN ProductItem pi ON pi.item_product_id = i.item_id
                                    WHERE p.product_id = pi.product_item_id
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
        return product_data

    def return_one_product(self, id):
        cursor = mydb.cursor()
        sql = ('''SELECT JSON_OBJECT (
                                "id", p.product_id,
                                "name", p.product_name,
                                "items", IFNULL((
                                SELECT JSON_ARRAYAGG(JSON_OBJECT (
                                        "id", i.item_id,
                                        "name", i.item_name
                                        ))
                                        FROM Item i
                                        JOIN ProductItem pi ON pi.item_product_id = i.item_id
                                        WHERE p.product_id = pi.product_item_id
                                    ), JSON_ARRAY())
                                ) Product
                                FROM Product p WHERE p.product_id=%s''')
        cursor.execute(sql%id)
        data = cursor.fetchone()
        product = json.loads(data[0])
        id = product["id"]
        name = product["name"]
        items = []
        product_data = ProductData(id,name,items) 
        items = self.add_items(product["items"])
        for item in items:
             item_temp = ItemData(item.id, item.name)
             product_data.items.append(item_temp)
        return product_data
    