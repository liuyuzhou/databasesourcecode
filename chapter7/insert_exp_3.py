import pymongo

# mongo client
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
# 数据库连接，存在mongo_use则直接连接，不存在则创建
mongo_conn = mongo_client["mongo_use"]
# 集合获取，存在language_info集合则直接返回，不存在则创建
col_name = mongo_conn["language_info"]
# 插入值列表
insert_list = [
    {"_id": 1, "name": "Python", "web_site": "www.python.org"},
    {"_id": 2, "name": "BigData", "从业人员": 236783},
    {"_id": 3, "name": "AI", "人才需求": 500000},
]
# 插入指定 _id 的多个文档
result = col_name.insert_many(insert_list)
# 输出插入的所有文档对应的 _id 值
print('所有文档id值：\n{}'.format(result.inserted_ids))
# 查询集合中所有文档
query_all = col_name.find()
print('stu_info集合中的所有文档：')
for item in query_all:
    print(item)
