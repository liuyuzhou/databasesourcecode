# 从session_create.py文件中导入get_session函数
from chapter5.common.session_create import get_session
# 从course.py文件中导入Course类
from chapter5.common.course import Course


def table_insert():
    # 取得session对象
    session = get_session()
    # 创建 Course类实例
    course_obj = Course(course_name='Python', teacher_name='Teacher liu', class_times=32)
    # 添加对象
    session.add(course_obj)
    # 事务提交
    session.commit()


if __name__ == "__main__":
    table_insert()
