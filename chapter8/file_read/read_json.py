import os
import json

# 取得文件完整路径
json_file_path = os.path.join(os.getcwd(), 'files/basic_info.json')


def read_json_file():
    if os.path.exists(json_file_path) is False:
        return

    # 以读取方式打开json文件
    with open(json_file_path, 'r') as r_read:
        # 从json文件中读取内容，并用json模块中的load函数做转换
        read_result_dict = json.load(r_read)
        # 打印读取load所得文本的长度及类型
        print(len(read_result_dict), type(read_result_dict))
        # 取得对应键值
        content_list = read_result_dict.get('RECORDS')
        print(len(content_list), type(content_list))
        # 循环
        for item_dict in content_list:
            print(len(item_dict), type(item_dict))
            print(item_dict)
            full_path_id_str = item_dict.get('full_path_id')
            print(full_path_id_str)
            print('数字字符串：{}'.format(full_path_id_str))
            len_num_str = len(full_path_id_str)
            print('数字字符串长度：{}'.format(len_num_str))
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


if __name__ == "__main__":
    read_json_file()
