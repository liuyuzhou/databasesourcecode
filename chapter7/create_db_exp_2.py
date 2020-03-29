import pymongo

# mongo client
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
# 取得所有数据库名称
db_list = mongo_client.list_database_names()
if 'mongo_use' in db_list:
    print('database ({}) is exist.'.format('mongo_use'))
