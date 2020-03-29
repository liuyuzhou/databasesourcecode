from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 声明映射
Base = declarative_base()


# 定义Course对象，课程表对象
class Course(Base):
    # 表的名字
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    course_name = Column(String(20), default=None, nullable=False, comment='课程名称')
    teacher_name = Column(String(20), default=None, nullable=False, comment='任课老师')
    class_times = Column(Integer, default=0, nullable=False, comment='课时')

    # 定义__repr__函数，返回一个可以用来表示对象的可打印字符串
    def __repr__(self):
        c_name = self.course_name
        t_name = self.teacher_name
        c_times = self.class_times
        return f"Course:(course_name={c_name}, teacher_name={t_name}, class_times={c_times})"
