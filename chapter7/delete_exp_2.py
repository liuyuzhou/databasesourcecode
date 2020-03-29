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
    mongo_col = mongo_conn["stu_info"]
    return mongo_col


def delete_many_row():
    """
    删除多个文档
    :return: None
    """
    print('删除前：')
    query_all()
    # 集合获取，存在python_class集合则直接返回，不存在则创建
    mongo_col = get_col()
    # 查询条件
    condition_dict = {"number": {"$gt": 1003}}
    mongo_col.delete_many(condition_dict)
    print('删除后：')
    query_all()


def query_all():
    """
    查询集合中所有数据
    :return: None
    """
    # 查询集合中所有数据
    all_result = get_col().find()
    # 输出修改后的python_class集合
    for item in all_result:
        print(item)


if __name__ == "__main__":
    delete_many_row()
