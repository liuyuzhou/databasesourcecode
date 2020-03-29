import pymongo


def get_col():
    """
    取得指定集合
    :return: 指定集合
    """
    # mongo client
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    # 数据库连接，存在data_school则直接连接，不存在则创建
    mongo_conn = mongo_client["data_school"]
    # 集合获取，存在basic_info集合则直接返回，不存在则创建
    mongo_col = mongo_conn["basic_info"]
    return mongo_col
