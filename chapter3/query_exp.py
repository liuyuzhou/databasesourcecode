import pymysql


def query_record():
    """
    记录查询
    :return:
    """
    # 打开数据库连接，不添加端口号写法
    db = pymysql.connect("localhost", "root", "root", "data_school")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM st_addr"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id_v = row[0]
            num = row[1]
            addr = row[2]
            # 打印结果
            print(f"详细信息为:id={id_v},number={num},addr={addr}")
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    query_record()
