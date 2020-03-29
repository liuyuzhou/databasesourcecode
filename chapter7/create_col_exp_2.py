import pymongo

# mongo client
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
# 取得数据库
mongo_conn = mongo_client["mongo_use"]
# 取得所有数据库名称
col_list = mongo_conn.list_collection_names()
if 'python_class' in col_list:
    print('collection ({}) is exist.'.format('python_class'))
