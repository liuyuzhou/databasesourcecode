from sqlalchemy import create_engine, Column, String, Integer, func, DateTime, BIGINT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def get_db_conn_info():
    # "mysql+pymysql://用户名:密码@ip地址/数据库名?charset=UTF8MB4"
    conn_info_r = "mysql+pymysql://root:root@localhost/data_school?charset=UTF8MB4"
    return conn_info_r


conn_info = get_db_conn_info()
engine = create_engine(conn_info, echo=True)

db_session = sessionmaker(bind=engine)
session = db_session()
BaseModel = declarative_base()


class BasicInfo(BaseModel):
    __tablename__ = "basic_info"
    id = Column(Integer, primary_key=True)
    image_id = Column(Integer, default=0, nullable=True, comment='图片id')
    product_code = Column(String(200), default=None, nullable=True, comment='产品代码')
    full_path_id = Column(String(100), default=None, nullable=True, comment='类目结构')
    en_name = Column(String(100), default=None, nullable=True, comment='英文名')
    full_path_en_name = Column(String(200), default=None, nullable=True, comment='全类目英文名')
    file_path = Column(String(300), default=None, nullable=True, comment='路径')
    modify_timestamp = Column(BIGINT, default=0, nullable=False, comment='时间戳')
    create_date = Column(DateTime, default=func.now(), nullable=False, comment='创建时间')
    update_date = Column(DateTime, nullable=True, comment='更改时间')


BaseModel.metadata.create_all(engine)
