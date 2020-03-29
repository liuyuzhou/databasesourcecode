from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建Session
Session = sessionmaker(twophase=True)
# 创建连接引擎
engine_1 = create_engine('mysql+pymysql://root:root@localhost:3306/test1?charset=utf8', echo=True)
engine_2 = create_engine('mysql+pymysql://root:root@localhost:3306/test2?charset=utf8', echo=True)
Session.configure(bind=engine_1)
Session.configure(binds={Object_1: engine_1, Object_2: engine_2})
# 构造新的Session
session = Session()
