import docx
import os

# 取得文件完整路径
file_path = os.path.join(os.getcwd(), 'files/basic_info.doc')


def read_word_file():
    doc = docx.Document(file_path)
    # 遍历所有表格
    for table in doc.tables:
        # 遍历表格的所有行
        for row in table.rows:
            # 一行数据
            row_str = '\t'.join([cell.text for cell in row.cells])
            print(type(row.cells), len(row.cells))
            print(row.cells[2].text)
            print(row_str)

            full_path_id_str = row.cells[2].text
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
            print('代码量少的转换结果：{}'.format(simple_num_list))

            # 创建一个list对象
            num_list = list()
            for str_i in num_str_2_list:
                num_i = int(str_i)
                num_list.append(num_i)
            print('代码量多，但代码比较清晰易读，转换结果：{}'.format(num_list))


if __name__ == "__main__":
    read_word_file()
