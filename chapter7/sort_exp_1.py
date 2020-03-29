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
    执行排序
    :return: None
    """
    # 集合获取，存在python_class集合则直接返回，不存在则创建
    mongo_col = get_col()
    # 升序排序
    obj_asce_sort = mongo_col.find().sort("number")
    print('升序排序结果：')
    for item in obj_asce_sort:
        print(item)

    # 降序排序
    obj_desc_sort = mongo_col.find().sort("number", -1)
    print('降序排序结果：')
    for item in obj_desc_sort:
        print(item)


if __name__ == "__main__":
    execute_sort()
