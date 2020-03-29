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
    query_result = session.query(Course).filter(Course.course_name == 'Python')
    for item in query_result:
        print(f'查询结果为==>{item}')
        print(f'item对象的类型为:{type(item)}')
        print(f'更改前：teacher_name={item.teacher_name}')
        # 将 Teacher liu 更改为 Teacher LI
        item.teacher_name = 'Teacher LI'
        session.add(item)
        session.commit()

    query_result = session.query(Course).filter(Course.course_name == 'Python')
    for item in query_result:
        print(f'更改后：teacher_name={item.teacher_name}')


if __name__ == "__main__":
    table_update()
