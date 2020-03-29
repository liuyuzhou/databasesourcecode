import pymysql

# 打开数据库连接，不加端口号写法
# db = pymysql.connect("localhost", "root", "root", "data_school")
# 打开数据库连接，添加端口号写法
# db = pymysql.connect("localhost", "root", "root", "data_school", 3306)
# 打开数据库连接，显示指明参数名写法
db = pymysql.connect(host="localhost", user="root", password="root", database="data_school", port=3306)
# 使用数据库连接对象的 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用游标对象的 execute() 方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用游标对象的 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print(f"Database version:{data}")
# 关闭数据库连接
db.close()
