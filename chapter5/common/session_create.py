from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session():
    """
    创建session并返回
    :return: session 对象
    """
    # 创建Session
    connect_str = 'mysql+pymysql://root:root@localhost:3306/data_school?charset=utf8'
    Session = sessionmaker()
    # 创建连接引擎
    engine = create_engine(connect_str, echo=True)
    Session.configure(bind=engine)
    # 构造新的Session
    session = Session()
    return session
