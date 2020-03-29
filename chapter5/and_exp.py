# 从session_create.py文件中导入get_session函数
from chapter5.common.session_create import get_session
# 从course.py文件中导入Course类
from chapter5.common.course import Course
from sqlalchemy import and_


def table_query():
    """
    表数据查询
    :return:
    """
    # 取得session对象
    session = get_session()
    # 方法一：使用 and_()
    query_result = session.query(Course).\
        filter(and_(Course.teacher_name == 'Teacher Wang', Course.course_name == 'MySQL'))
    # 方法二：在filter()中设置多个表达式
    query_result = session.query(Course).\
        filter(Course.teacher_name == 'Teacher Wang', Course.course_name == 'MySQL')
    # 方法三：使用多个filter()
    query_result = session.query(Course).filter(Course.teacher_name == 'Teacher Wang').\
        filter(Course.course_name == 'MySQL')
    for item in query_result:
        print(f'查询结果为==>{item}')


if __name__ == "__main__":
    table_query()
