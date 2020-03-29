import pymysql


def mysql_select():
    """
    数据查找
    :return:
    """
    # 打开数据库连接，添加端口号写法
    db = pymysql.connect("localhost", "root", "root", "data_school", 3306)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 待查询的学号
    s_num = 1002
    # SQL 查询语句
    sql = "SELECT * FROM python_class WHERE number = {}".format(s_num)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            num = row[1]
            name = row[2]
            cs_name = row[3]
            # 打印结果
            print(f"学号为{s_num}的详细信息为:"
                  f"number={num},name={name},class_name={cs_name}")
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    mysql_select()
