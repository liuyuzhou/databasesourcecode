import time
import csv
import datetime
import os

from chapter8.database.sqlalchemy_conn import db_conn
from chapter8.database.model_obj import BasicInfo

csv_file_path = os.path.join(os.getcwd(), 'files/query_hive.csv')


# 读取csv文件
def read_csv_file():
    start_time = time.time()
    # 打开文件并读取内容
    with open(csv_file_path, 'r') as r_read:
        # 读取csv文件所有内容
        file_read = csv.reader(r_read)
        # 按行遍历读取内容
        row_count = 0
        # 按行读取csv文件内容，并按行插入mysql
        for row in file_read:
            if row_count == 0:
                row_count += 1
                print(row)
                continue

            row_count += 1
            image_id = row[0]
            file_path = row[1]
            modify_timestamp = row[2]
            product_code = row[3]
            en_name = row[4]
            full_path_id = row[5]
            full_path_en_name = row[6]
            try:
                session = db_conn()
                # 构造插入数据库的语句
                basic_info_obj = BasicInfo(image_id=image_id, file_path=file_path,
                                           modify_timestamp=modify_timestamp,
                                           product_code=product_code,
                                           en_name=en_name, full_path_id=full_path_id,
                                           full_path_en_name=full_path_en_name,
                                           create_date=datetime.datetime.now())
                # 数据按行插入数据库
                session.add(basic_info_obj)
                session.commit()
                session.close()
            except Exception as ex:
                print('insert error:{}'.format(ex))
        print('插入({0})条记录，花费：{1}s'.format(row_count - 1, time.time() - start_time))


if __name__ == "__main__":
    read_csv_file()
