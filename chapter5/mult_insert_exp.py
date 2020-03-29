# 从session_create.py文件中导入get_session函数
from chapter5.common.session_create import get_session
# 从course.py文件中导入Course类
from chapter5.common.course import Course


def table_insert():
    # 取得session对象
    session = get_session()
    # 创建 Course类实例
    course_obj_1 = Course(course_name='MySQL', teacher_name='Teacher Wang', class_times=32)
    course_obj_2 = Course(course_name='PyMySQL', teacher_name='Teacher Zhang', class_times=32)
    course_obj_3 = Course(course_name='SQLAlchemy', teacher_name='Teacher Gao', class_times=32)
    # 添加多个对象
    session.add_all([course_obj_1, course_obj_2, course_obj_3])
    # 事务提交
    session.commit()


if __name__ == "__main__":
    table_insert()
