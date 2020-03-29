import pymongo

# mongo client
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
# 数据库连接，存在mongo_use则直接连接，不存在则创建
mongo_conn = mongo_client["mongo_use"]
# 集合获取，存在stu_info集合则直接返回，不存在则创建
col_name = mongo_conn["stu_info"]
# 插入值字典
insert_dict = {"name": "小强", "number": 1001, "email": "xiaoqiang@abc.com"}
# 集合中插入一个文档
result = col_name.insert_one(insert_dict)
# print(result)
print(result.inserted_id)
# 查询集合中所有文档
query_all = col_name.find()
for item in query_all:
    print(item)
