# 从session_create.py文件中导入get_session函数
from chapter5.common.session_create import get_session
# 从course.py文件中导入Course类
from chapter5.common.course import Course
from sqlalchemy import func


def table_query():
    """
    表数据查询
    :return:
    """
    # 取得session对象
    session = get_session()
    # 数据查询
    # query_result = session.query(func.count(Course.course_name), Course.course_name).group_by(Course.course_name).all()
    # query_result = session.query(func.count('*')).select_from(Course).scalar()
    query_result = session.query(func.count(Course.id)).scalar()
    print(f'查询结果为==>{query_result}')


if __name__ == "__main__":
    table_query()
