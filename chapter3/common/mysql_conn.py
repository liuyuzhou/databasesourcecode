import pymysql


class MySQLConnection(object):
    """
    MySQL连接
    """
    def __init__(self, host=None, user=None, password=None, database=None, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.db = self.get_db()
        self.conn = self.conn

    def get_db(self):
        """
        打开数据库连接
        :return:
        """
        db = pymysql.connect(self.host, self.user, self.password, self.database, self.port)
        return db

    def conn(self):
        """
        使用cursor()方法获取操作游标
        :return:
        """
        cursor = self.db.cursor()
        return cursor

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        self.db.close()

    def query_all(self, query_sql):
        """
        根据查询语句查询所有数据
        :param query_sql:
        :return:
        """
        try:
            cursor = self.conn()
            # 执行SQL语句
            cursor.execute(query_sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            return results
        except Exception as ex:
            print("query all Error: {}".format(ex))
        finally:
            self.close()

    def query_one(self, query_sql):
        """
        根据查询语句查询一条语句
        :param query_sql:
        :return:
        """
        try:
            cursor = self.conn()
            # 执行SQL语句
            cursor.execute(query_sql)
            # 获取一条记录
            results = cursor.fetchone()
            return results
        except Exception as ex:
            print("query all Error: {}".format(ex))
        finally:
            self.close()

    def update(self, update_sql):
        """
        根据更新语句更新数据
        :param update_sql:
        :return:
        """
        try:
            cursor = self.conn()
            # 执行SQL语句
            cursor.execute(update_sql)
            # 提交到数据库执行
            self.db.commit()
        except Exception as ex:
            print("update Error: {}".format(ex))
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.close()


if __name__ == "__main__":
    sql_ = "select * from python_class"
    conn = MySQLConnection("localhost", "root", "root", "data_school")
    result = conn.query_all(sql_)
    print(result)
    for item in result:
        print(item)

    # conn = MySQLConnection("localhost", "root", "root", "data_school")
    # sql = "UPDATE python_class SET name = '{}' WHERE name = '{}'".format('小李', '小张')
    # sql = """INSERT INTO python_class(number,name, class_name)
    #              VALUES (1005, '小张', 'python快乐学习班')"""
    # conn.update(sql)
