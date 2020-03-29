import pymysql


def create_table():
    """
    创建表
    :return:
    """
    # 打开数据库连接，添加端口号写法
    db = pymysql.connect("localhost", "root", "root", "data_school", 3306)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用预处理语句创建表
    sql = """CREATE TABLE st_addr (
             id INT UNSIGNED AUTO_INCREMENT,
             number INT(10) NOT NULL,
             addr VARCHAR(100) NOT NULL,
             PRIMARY KEY (id)
             )ENGINE=InnoDB DEFAULT CHARSET=utf8"""

    cursor.execute(sql)

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    create_table()
