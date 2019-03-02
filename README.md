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

# Import tables from mySql to Hadoop cluster
sqoop import --connect "jdbc:mysql://SOURCE/dbname" --username USERNAME --password PASSWORD --table orders --target-dir /TARGET_LOCATION/orders
sqoop import --connect "jdbc:mysql://SOURCE/dbname" --username USERNAME --password PASSWORD --table order_items --target-dir /TARGET_LOCATION/order_items
