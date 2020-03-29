import os

# 取得文件完整路径
txt_file_path = os.path.join(os.getcwd(), 'files/basic_info.txt')


# 定义一个函数
def read_txt_file():
    # 检查 txt 文件是否存在
    if os.path.exists(txt_file_path) is False:
        return

    # 以读取方式打开txt文件
    with open(txt_file_path, 'r') as r_read:
        # 遍历读取文本内容
        for row in r_read:
            # 打印读取的原始行
            print('分割前数据：{}'.format(row))
            # 对原始行根据空格进行分割
            f_list = row.split(' ')
            # 打印分割的结果列表
            print('根据空格进行分割所得结果为：{}'.format(f_list))
            # 对原始行根据制表符\t 分割
            field_list = row.split("\t")
            print('根据制表符进行分割所得结果为：{}'.format(field_list))
            # 对原始行 " 号用空白替换，对原始行 换行符 \n 用空白替换
            row = row.replace('"', '').replace('\n', '')
            # 替换后的行根据制表符\t 分割
            replace_field_list = row.split('\t')
            print('替换后分割结果：{}'.format(replace_field_list))
            print('列表长度：{}'.format(len(replace_field_list)))
            full_path_id_str = replace_field_list[2]
            print('数字字符串：{}'.format(full_path_id_str))
            len_num_str = len(full_path_id_str)
            print('数字字符串长度：{}'.format(len_num_str))
            num_str_1_list = full_path_id_str.split('|')
            print('数字字符串分割结果：{}'.format(num_str_1_list))
            # # 对数字字符串截取，从第一位截取到倒数第二位
            full_path_id_str = full_path_id_str[1: len_num_str - 1]
            print('截取后数字字符串：{}'.format(full_path_id_str))
            num_str_2_list = full_path_id_str.split('|')
            print('截取后数字字符串分割结果：{}'.format(num_str_2_list))
            # 创建一个list对象
            num_list = list()
            for str_i in num_str_2_list:
                num_i = int(str_i)
                num_list.append(num_i)
            print('转换结果：{}'.format(num_list))


if __name__ == "__main__":
    read_txt_file()
