import time
import csv
import os

from chapter8.database.sqlalchemy_conn import db_conn
from chapter8.database.model_obj import BasicInfo
from sqlalchemy import func

product_code_count_csv_file = os.path.join(os.getcwd(), 'files/product_count.csv')


# 数据查询统计
def query_from_mysql():
    try:
        session = db_conn()
        basic_info_group_list = session.query(BasicInfo.product_code, func.count(BasicInfo.product_code)).\
            group_by(BasicInfo.product_code)
        return basic_info_group_list
    except Exception as ex:
        print('insert error:{}'.format(ex))


# 查询结果处理，并将查询结果插入csv文件
def get_result_from_mysql():
    start_time = time.time()
    result_list = query_from_mysql()
    csv_data_list = list()
    for result in result_list:
        one_row_list = list()
        product_code = result[0]
        count_num = result[1]
        one_row_list.append(product_code)
        one_row_list.append(count_num)
        csv_data_list.append(one_row_list)

    with open(product_code_count_csv_file, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        for row in csv_data_list:
            writer.writerow(row)
    print('写入({0})条数据，花费：{1}s'.format(len(csv_data_list), time.time() - start_time))


if __name__ == "__main__":
    get_result_from_mysql()
