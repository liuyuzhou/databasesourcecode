import pymysql


def insert_record():
    """
    插入数据
    :return:
    """
    # 打开数据库连接，添加端口号写法
    db = pymysql.connect("localhost", "root", "root", "data_school", 3306)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = """INSERT INTO python_class(number,name, class_name)
             VALUES (1005, '小张', 'python快乐学习班')"""
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    insert_record()
