from sqlalchemy import create_engine

# 创建连接引擎
engine = create_engine('mysql+pymysql://root:root@localhost:3306/data_school?charset=utf8', echo=True)
