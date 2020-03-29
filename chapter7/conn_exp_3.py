import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db_list = mongo_client.list_database_names()
for item in db_list:
    print('本地MongoDB服务器中的数据库：{}'.format(item))
