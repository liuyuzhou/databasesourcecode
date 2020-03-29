# 从session_create.py文件中导入get_session函数
from chapter5.common.session_create import get_session
# 从course.py文件中导入Course类
from chapter5.common.course import Course


def table_delete():
    """
    表数据查询
    :return:
    """
    # 取得session对象
    session = get_session()
    # 数据查询
    course_obj = session.query(Course).filter(Course.course_name == 'Python').first()
    # print(course_obj)
    print(f'删除前==>{course_obj}')
    # 数据删除
    session.delete(course_obj)
    session.commit()

    course_obj = session.query(Course).filter(Course.course_name == 'Python').first()
    print(f'删除后==>{course_obj}')


if __name__ == "__main__":
    table_delete()
