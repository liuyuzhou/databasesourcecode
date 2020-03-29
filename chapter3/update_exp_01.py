import pymysql

# 打开数据库连接，添加端口号写法
db = pymysql.connect("localhost", "root", "root", "data_school", 3306)
# 使用cursor()方法获取操作游标
cursor = db.cursor()


def query_mysql(s_num):
    """
    根据条件查找数据
    :param s_num:
    :return:
    """
    # SQL 查询语句
    sql = "SELECT * FROM python_class WHERE number={}".format(s_num)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            num = row[1]
            name = row[2]
            # 打印结果
            print(f"学号为{s_num}的详细信息为:number={num},name={name}")
    except:
        print("Error: unable to fetch data")


def update_mysql():
    """
    数据更新
    :return:
    """
    # SQL 更新语句
    sql = "UPDATE python_class SET name = '{}' WHERE name='{}'".format('小李', '小张')
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


if __name__ == "__main__":
    number = 1005
    print("--------------更改之前---------------")
    query_mysql(number)
    update_mysql()
    print("--------------更改之后---------------")
    query_mysql(number)
    # 关闭数据库连接
    db.close()
