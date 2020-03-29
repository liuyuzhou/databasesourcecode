from chapter3.common.mysql_conn import MySQLConnection


def mysql_select():
    """
    数据查找
    :return:
    """
    # 待查询的学号
    s_num = 1002
    # SQL 查询语句
    sql = "SELECT * FROM python_class WHERE number = {}".format(s_num)
    try:
        # 获得数据库连接对象及游标
        conn = MySQLConnection("localhost", "root", "root", "data_school")
        # 执行SQL语句，并获取所有记录列表
        results = conn.query_all(sql)
        for row in results:
            num = row[1]
            name = row[2]
            cs_name = row[3]
            # 打印结果
            print(f"学号为{s_num}的详细信息为:"
                  f"number={num},name={name},class_name={cs_name}")
    except:
        print("Error: unable to fetch data")


if __name__ == "__main__":
    mysql_select()
