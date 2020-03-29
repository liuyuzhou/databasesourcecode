import pymongo


def get_db():
    """
    取得指定数据库
    :return: 指定数据库
    """
    # mongo client
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    # 数据库连接，存在mongo_use则直接连接，不存在则创建
    mongo_conn = mongo_client["mongo_use"]
    return mongo_conn


def get_all_col():
    """
    打印所有集合名
    :return: None
    """
    mongo_col_obj = get_db()
    col_list = mongo_col_obj.list_collection_names()
    for col in col_list:
        print('集合名：{}'.format(col))


def drop_col():
    """
    删除集合
    :return: None
    """
    print('删除集合stu_info前：')
    get_all_col()
    mongo_conn = get_db()
    mongo_col = mongo_conn["stu_info"]
    mongo_col.drop()
    print('删除集合stu_info后：')
    get_all_col()


if __name__ == "__main__":
    drop_col()
