# OrderSystem
* Problem statement - get the revenue and number of orders from order_items on daily basis
# Environment
* Hadoop 2.4 version
* Spark 1.2.1
* Python 2.6.6
# Tables info
* orders Table

| Field | Type | Null | Key | Default | Extra |
| ------| -----| -----| ----| --------| ------|
| order_id  | int(11) | NO | PRI | NULL | auto_increment |
|order_date | datetime | NO |   | NULL |   |
| order_customer_id | int(11) | NO |   | NULL |   |
| order_status | varchar(45) | NO |   | NULL |   |


* order_items Table

| Field | Type | Null | Key | Default | Extra |
| ------| -----| -----| ----| --------| ------|
| order_item_id | int(11) | NO | PRI | NULL | auto_increment |
| order_item_order_id | int(11) | NO |   | NULL |   |
| order_item_product_id | int(11) | NO |   | NULL |   |
| order_item_quantity | tinyint(4) | NO |   | NULL |   |
| order_item_subtotal | float | NO |   | NULL |   |
|order_item_product_price | float | NO |   | NULL |   |

* products Table

| Field | Type | Null | Key | Default | Extra |
| ------| -----| -----| ----| --------| ------|
| product_id | int(11) | NO | PRI | NULL | auto_increment |
| product_category_id | int(11)      | NO |   | NULL |   |
| product_name        | varchar(45)  | NO |   | NULL |   |
| product_description | varchar(255) | NO |   | NULL |   |
| product_price       | float        | NO |   | NULL |   |
| product_image       | varchar(255) | NO |   | NULL |   |

# Import tables from mySql to Hadoop cluster
* sqoop import --connect "jdbc:mysql://mysql/retail_db" --username USERNAME --password -P --table orders --target-dir /user/avmnrao/hadoop/python/orders
* sqoop import --connect "jdbc:mysql://mysql/retail_db" --username USERNAME --password -P --table order_items --target-dir /user/avmnrao/hadoop/python/order_items
* sqoop import --connect "jdbc:mysql://mysql/retail_db" --username USERNAME --password -P --table products --target-dir /user/avmnrao/hadoop/python/products

