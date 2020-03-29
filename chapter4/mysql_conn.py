from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:root@localhost:3306/data_school?charset=utf8', echo=True)
# 声明映射
Base = declarative_base()
