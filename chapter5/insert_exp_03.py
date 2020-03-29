from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# 从course.py文件中导入Course类
from chapter5.common.course import Course

# 创建Session
Session = sessionmaker()
# 创建连接引擎
engine = create_engine('mysql+pymysql://root:root@localhost:3306/data_school?charset=utf8', echo=True)
Session.configure(bind=engine)
# 构造新的Session
session = Session()

# 创建 Course类实例
course_obj = Course(course_name='Python', teacher_name='Teacher liu', class_times=32)
# 添加对象
session.add(course_obj)
# 事务提交
session.commit()

