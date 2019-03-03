# Data Conversion from jSon to parquet
# imported products table data from source to hadoop inn jSon format
# import packages

from pyspark.sql import SQLContext
from pyspark.sql.types import *
sqlContext = SQLContext(sc)

# imported jSon data saving on parquet format
df = sqlContext.read.load("user/avmnrao/hadoop/python/productsAvro.json", format="json")
df.select("product_id", "product_name", "product_price").write.save("productsParq.parquet", format="parquet")
