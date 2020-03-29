import pymysql


def query_mysql(num):
    """
    记录查询
    :return:
    """
    # 打开数据库连接，不添加端口号写法
    db = pymysql.connect("localhost", "root", "root", "data_school")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT a.number,a.name,b.addr FROM python_class a " \
          "JOIN st_addr b ON a.number=b.number AND a.number={}".format(num)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            num_v = row[0]
            name = row[1]
            addr = row[2]
            # 打印结果
            print(f"学号为{num}的详细信息为:number={num_v},name={name},addr={addr}")
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    query_mysql(1002)
