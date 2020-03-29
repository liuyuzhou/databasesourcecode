from chapter3.common.mysql_conn import MySQLConnection


def get_conn():
    # 获得数据库连接对象及游标
    conn = MySQLConnection("localhost", "root", "root", "data_school")
    return conn


def query_mysql(s_num):
    """
    根据条件查找数据
    :param s_num:
    :return:
    """
    # SQL 查询语句
    sql = "SELECT * FROM python_class WHERE number={}".format(s_num)
    try:
        # 执行SQL语句，并获取所有记录列表
        results = get_conn().query_all(sql)
        for row in results:
            num = row[1]
            name = row[2]
            # 打印结果
            print(f"学号为{s_num}的详细信息为:number={num},name={name}")
    except Exception as ex:
        print("query Error: {}".format(ex))


def update_mysql():
    """
    数据更新
    :return:
    """
    # SQL 更新语句
    sql = "UPDATE python_class SET name = '{}' WHERE name='{}'".format('小李', '小张')
    try:
        # 执行SQL语句
        get_conn().update(sql)
        # 提交到数据库执行
    except Exception as ex:
        print("update Error: {}".format(ex))


if __name__ == "__main__":
    number = 1005
    print("--------------更改之前---------------")
    query_mysql(number)
    update_mysql()
    print("--------------更改之后---------------")
    query_mysql(number)
