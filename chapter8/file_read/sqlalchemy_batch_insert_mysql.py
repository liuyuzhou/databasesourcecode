import time
import csv
import datetime
import os

from chapter8.database.sqlalchemy_conn import db_conn
from chapter8.database.model_obj import BasicInfo

csv_file_path = os.path.join(os.getcwd(), 'files/query_hive.csv')


def lines_count():
    """
    csv文件总行数统计
    :return: 总行数
    """
    f_read = open(csv_file_path, "r")
    cline = 0
    while True:
        buffer = f_read.read(8*1024*1024)
        if not buffer:
            break
        cline += buffer.count('\n')
    f_read.seek(0)
    return cline


# 读取csv文件
def read_csv_file():
    start_time = time.time()
    # csv文件总行数统计
    total_line = lines_count()
    # 打开文件并读取内容
    with open(csv_file_path, 'r') as r_read:
        # 读取csv文件所有内容
        file_read = csv.reader(r_read)
        # 按行遍历读取内容
        row_count = 0
        basic_info_obj_list = list()
        for row in file_read:
            if row_count == 0:
                row_count += 1
                print(row)
                continue

            image_id = row[0]
            file_path = row[1]
            modify_timestamp = row[2]
            product_code = row[3]
            en_name = row[4]
            full_path_id = row[5]
            full_path_en_name = row[6]

            basic_info_obj = BasicInfo(image_id=image_id, file_path=file_path,
                                       modify_timestamp=modify_timestamp,
                                       product_code=product_code, en_name=en_name,
                                       full_path_id=full_path_id,
                                       full_path_en_name=full_path_en_name,
                                       create_date=datetime.datetime.now())
            basic_info_obj_list.append(basic_info_obj)
            row_count += 1
            # 每1000条记录做一次插入
            if row_count % 1000 == 0:
                batch_insert_into_mysql(basic_info_obj_list)
                basic_info_obj_list.clear()
                continue

            # 剩余数据插入数据库
            if row_count == total_line:
                batch_insert_into_mysql(basic_info_obj_list)
                basic_info_obj_list.clear()

        print('插入({0})条记录，花费：{1}s'.format(row_count - 1, time.time() - start_time))


# 数据批量插入数据库
def batch_insert_into_mysql(basic_info_obj_list):
    try:
        session = db_conn()
        session.add_all(basic_info_obj_list)
        session.commit()
        session.close()
    except Exception as ex:
        print('batch insert error:{}'.format(ex))


if __name__ == "__main__":
    read_csv_file()
