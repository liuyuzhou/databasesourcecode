# 从session_create.py文件中导入get_session函数
from chapter5.common.session_create import get_session
# 从course.py文件中导入Course类
from chapter5.common.course import Course


def table_update():
    """
    数据查询并修改
    :return:
    """
    # 取得session对象
    session = get_session()
    # 数据查询
    course_obj = session.query(Course).filter(Course.course_name == 'Python').first()
    print(course_obj)
    print(type(course_obj))
    print(f'更改前：teacher_name={course_obj.teacher_name}')
    # 将 Teacher LI 更改为 Teacher LIU
    course_obj.teacher_name = 'Teacher LIU'
    session.add(course_obj)
    session.commit()

    course_obj = session.query(Course).filter(Course.course_name == 'Python').first()
    print(course_obj)
    print(f'更改后：teacher_name={course_obj.teacher_name}')


if __name__ == "__main__":
    table_update()
