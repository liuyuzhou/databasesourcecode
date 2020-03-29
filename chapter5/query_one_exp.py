# 从session_create.py文件中导入get_session函数
from chapter5.common.session_create import get_session
# 从course.py文件中导入Course类
from chapter5.common.course import Course


def table_query():
    """
    表数据查询
    :return:
    """
    # 取得session对象
    session = get_session()
    # 返回多于一个查询结果
    # query_result = session.query(Course).one()
    # 没有查询结果
    # query_result = session.query(Course).filter(Course.course_name == 'Python').one()
    # 返回一个查询结果
    query_result = session.query(Course).filter(Course.course_name == 'MySQL').one()
    print(f'查询结果为==>{query_result}')


if __name__ == "__main__":
    table_query()
