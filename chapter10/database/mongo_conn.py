import pymongo


def get_mongo_conn():
    """
    取得数据库连接
    :return: 指定数据库
    """
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    # 数据库连接，存在data_school则直接连接，不存在则创建
    mongo_conn = mongo_client["data_school"]
    return mongo_conn


def col_singer_song():
    """
    取得指定集合
    :return: 指定集合
    """
    mongo_conn = get_mongo_conn()
    # 集合获取，存在singer_song集合则直接返回，不存在则创建
    mongo_col = mongo_conn["singer_song"]
    return mongo_col


def col_song():
    """
    取得指定集合
    :return: 指定集合
    """
    mongo_conn = get_mongo_conn()
    # 集合获取，存在song集合则直接返回，不存在则创建
    mongo_col = mongo_conn["song"]
    return mongo_col
