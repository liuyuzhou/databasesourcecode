import os
import csv
import datetime

# 取得文件完整路径
csv_file_path = os.path.join(os.getcwd(), 'files/basic_info.csv')


# 读取csv文件
def read_csv_file():
    # 判断对应路径下文件是否存在
    if os.path.exists(csv_file_path) is False:
        return

    # 以读取方式打开csv文件
    with open(csv_file_path, 'r') as r_read:
        # 读取csv文件所有内容
        file_read = csv.reader(r_read)
        # 按行遍历读取内容
        for row in file_read:
            # 查看每行类型及每行长度
            print('csv文件读取一行的类型为：{}，读取一行长度：{}'.format(type(row), len(row)))
            print('csv文件读取一行的内容：{}'.format(row))
            # 取得一行中的第三列元素
            full_path_id_str = row[2]
            print(full_path_id_str)
            print('数字字符串：{}'.format(full_path_id_str))
            # 字符串长度
            len_num_str = len(full_path_id_str)
            print('数字字符串长度：{}'.format(len_num_str))
            # 字符串分割
            num_str_1_list = full_path_id_str.split('|')
            print('数字字符串分割结果：{}'.format(num_str_1_list))
            # 对数字字符串截取，从第一位截取到倒数第二位
            num_str = full_path_id_str[1: len_num_str - 1]
            print('截取后数字字符串：{}'.format(num_str))
            num_str_2_list = num_str.split('|')
            print('截取后数字字符串分割结果：{}'.format(num_str_2_list))
            # 直接做转换，代码量少，结果不容易一眼看出
            simple_num_list = [int(s) for s in num_str_2_list]
            print('代码量少的转换结果：{}'.format(simple_num_list))

            # 创建一个list对象
            num_list = list()
            for str_i in num_str_2_list:
                num_i = int(str_i)
                num_list.append(num_i)
            print('代码量多，但代码比较清晰易读，转换结果：{}'.format(num_list))
            #
            # # 取得读取文件中的时间
            create_time_str = row[7]
            # # 打印字符串的值，并打印字符串类型
            print(create_time_str, type(create_time_str))
            # # 对字符串做类型及格式转换
            create_time = datetime.datetime.strptime(create_time_str, "%Y/%m/%d %H:%M:%S")
            print(create_time, type(create_time))


if __name__ == "__main__":
    read_csv_file()
