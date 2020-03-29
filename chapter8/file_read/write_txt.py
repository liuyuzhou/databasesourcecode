import os

txt_file_path = os.path.join(os.getcwd(), 'files/basic_info.txt')
write_txt_file_path = os.path.join(os.getcwd(), 'files/write_txt_file.txt')


# 定义一个函数
def write_txt_file():
    # 检查 txt 文件是否存在
    if os.path.exists(txt_file_path) is False:
        return

    with open(txt_file_path, 'r') as r_read:
        for row in r_read:
            # 打印读取的原始行
            print(row)
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
            # 对数字字符串截取，从第一位截取到倒数第二位
            full_path_id_str = full_path_id_str[1: len_num_str - 1]
            print('截取后数字字符串：{}'.format(full_path_id_str))
            num_str_2_list = full_path_id_str.split('|')
            print('截取后数字字符串分割结果：{}'.format(num_str_2_list))
            # 直接做转换，代码量少，结果不容易一眼看出
            simple_num_list = [int(s) for s in num_str_2_list]
            simple_num_str_list = [s for s in num_str_2_list]
            print('转换结果：{}'.format(simple_num_list))

            # mode='w'，写方式，mode='a'，追加方式打开json文件
            with open(write_txt_file_path, mode='a') as w_file:
                # 写入数据
                w_file.write(','.join(simple_num_str_list))
                # 换行
                w_file.write('\n')
                print('write sucess.')


if __name__ == "__main__":
    write_txt_file()
