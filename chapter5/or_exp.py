# 从session_create.py文件中导入get_session函数
from chapter5.common.session_create import get_session
# 从course.py文件中导入Course类
from chapter5.common.course import Course
from sqlalchemy import or_


def table_query():
    """
    表数据查询
    :return:
    """
    # 取得session对象
    session = get_session()
    # 使用 or_()
    query_result = session.query(Course).\
        filter(or_(Course.teacher_name == 'Teacher Wang', Course.course_name == 'SQLAlchemy'))
    for item in query_result:
        print(f'查询结果为==>{item}')


if __name__ == "__main__":
    table_query()
