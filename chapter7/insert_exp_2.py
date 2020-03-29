import pymongo

# mongo client
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
# 数据库连接，存在mongo_use则直接连接，不存在则创建
mongo_conn = mongo_client["mongo_use"]
# 集合获取，存在stu_info集合则直接返回，不存在则创建
col_name = mongo_conn["stu_info"]
# 插入值列表
insert_list = [
    {"name": "小王", "number": 1002, "phone": 15217639876},
    {"name": "小李", "number": 1003, "address": "beijing"},
    {"name": "小张", "number": 1004, "habit": "旅游，看书", "email": "xiaozhang@abc.com"},
    {"name": "小刘", "number": 1005, "qq": 123456, "email": "xiaoliu@123.com"}
]
# 集合中插入多个文档
result = col_name.insert_many(insert_list)
# 输出插入的所有文档对应的 _id 值
print('所有文档id值：\n{}'.format(result.inserted_ids))
# 查询集合中所有文档
query_all = col_name.find()
print('stu_info集合中的所有文档：')
for item in query_all:
    print(item)
