import pymongo


def get_col():
    """
    取得指定集合
    :return: 指定集合
    """
    # mongo client
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    # 数据库连接，存在mongo_use则直接连接，不存在则创建
    mongo_conn = mongo_client["mongo_use"]
    # 集合获取，存在python_class集合则直接返回，不存在则创建
    mongo_col = mongo_conn["python_class"]
    return mongo_col


def execute_sort():
    """
    更新一个文档
    :return: None
    """
    # 集合获取，存在python_class集合则直接返回，不存在则创建
    mongo_col = get_col()
    # 排序
    obj_sort = mongo_col.find().sort([
        ("name", pymongo.DESCENDING),
        ("number", pymongo.DESCENDING)])
    for item in obj_sort:
        print(item)


if __name__ == "__main__":
    execute_sort()
