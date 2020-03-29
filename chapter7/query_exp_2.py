import pymongo

# mongo client
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
# 数据库连接，存在mongo_use则直接连接，不存在则创建
mongo_conn = mongo_client["mongo_use"]
# 集合获取，存在python_class集合则直接返回，不存在则创建
mongo_col = mongo_conn["python_class"]
# 查询集合中所有数据
query_all = mongo_col.find()
for item in query_all:
    print(item)
