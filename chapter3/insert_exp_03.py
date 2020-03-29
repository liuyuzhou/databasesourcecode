from chapter3.common.mysql_conn import MySQLConnection


def get_conn():
    # 获得数据库连接对象及游标
    conn = MySQLConnection("localhost", "root", "root", "data_school")
    return conn


def insert_record():
    """
    插入数据
    :return:
    """
    # SQL 插入语句
    sql = """INSERT INTO python_class(number,name, class_name)
             VALUES (1006, '小王', 'python快乐学习班')"""
    try:
        # 执行sql语句
        get_conn().update(sql)
        print('记录插入成功。')
    except Exception as ex:
        print("update Error: {}".format(ex))


if __name__ == "__main__":
    insert_record()
