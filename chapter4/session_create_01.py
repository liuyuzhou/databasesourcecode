from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建连接引擎
engine = create_engine('mysql+pymysql://root:root@localhost:3306/data_school?charset=utf8', echo=True)
# 创建Session
Session = sessionmaker(bind=engine)
# 构造新的Session
session = Session()
