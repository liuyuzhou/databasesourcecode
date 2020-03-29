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


def one_update():
    """
    更新一个文档
    :return: None
    """
    print('更改文档前，文档中数据：')
    query_all()
    # 集合获取，存在python_class集合则直接返回，不存在则创建
    mongo_col = get_col()
    # 查询条件
    condition_dict = {"number": 1004}
    # 新name值
    new_name = {"$set": {"name": "小李"}}
    # 更新
    obj = mongo_col.update_one(condition_dict, new_name)
    print("共修改{}个文档".format(obj.modified_count))
    print('更改文档后，文档中数据：')
    query_all()


if __name__ == "__main__":
    one_update()
