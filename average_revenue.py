import sys
from operator import add
from pyspark.sql import SparkSession
from pyspark import SQLContext

# Read the Orders and Order_Items data
orders_RDD = sc.textFile("/TARGET_LOCATION/orders")
orderItems_RDD = sc.textFile("/TARGET_LOCATION/order_items")

# fetch the required field (key Order_id)
ordersFetch = orders_RDD.map(lambda rec: (rec.split(",")[0], rec))
# fetch the required field (key Order_item_order_id)
orderItemsFetch = orderItems_RDD.map(lambda rec: (rec.split(",")[1], rec))

# Join both Order and Order_Items datasets
ordersJoinOrderItems = orderItemsFetch.join(ordersFetch)

#Parse joined data and get (order_date, order_id) as key  and order_item_subtotal as value 
revenuePerOrderPerDay = ordersJoinOrderItems.map(lambda t: ((t[1][1].split(",")[1], t[0]), float(t[1][0].split(",")[4])))

# Get the order count per day
ordersPerDay = ordersJoinOrderItems.map(lambda rec: rec[1][1].split(",")[1] + "," + str(rec[0])).distinct()
# Parse joined data and get (order_date, order_id) as key  and order_item_subtotal as value
ordersPerDayParsedRDD = ordersPerDay.map(lambda rec: (rec.split(",")[0], 1))
totalOrdersPerDay = ordersPerDayParsedRDD.reduceByKey(lambda x, y: x + y)

# Get revenue per day from joined data
totalRevenuePerDay = revenuePerOrderPerDay.reduceByKey(lambda total1, total2: total1 + total2)
for data in totalRevenuePerDay.collect():
  print(data)

# Joining order count per day and revenue per day
finalJoinRDD = totalOrdersPerDay.join(totalRevenuePerDay)
for revenue in finalJoinRDD.take(5):
  print(revenue)
