import pymysql


def batch_insert():
    """
    数据批量插入
    :return:
    """
    # 打开数据库连接，添加端口号写法
    db = pymysql.connect("localhost", "root", "root", "data_school", 3306)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    st_1_addr = "(1001, 'A城区')"
    st_2_addr = "(1002, 'B城区')"
    st_3_addr = "(1003, 'C城区')"
    # SQL 插入语句
    sql = "INSERT INTO st_addr (number,addr) VALUES "
    sql += st_1_addr
    sql += ',' + st_2_addr
    sql += ',' + st_3_addr
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    batch_insert()
