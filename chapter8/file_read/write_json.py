import os
import json

json_file_path = os.path.join(os.getcwd(), 'files/basic_info.json')
write_json_file_path = os.path.join(os.getcwd(), 'files/write_json_file.json')


def read_json_file():
    if os.path.exists(json_file_path) is False:
        return

    with open(json_file_path, 'r') as r_read:
        # 从json文件中读取内容，并用json模块中的load函数做转换
        read_result_dict = json.load(r_read)

        # mode='w'，写方式，mode='a'，追加方式打开json文件
        with open(write_json_file_path, mode='a') as w_file:
            # 通过json中的dumps函数将数据转换为json格式写入json文件
            w_file.write(json.dumps(read_result_dict))


if __name__ == "__main__":
    read_json_file()
