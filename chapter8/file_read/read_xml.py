import os
import xml.dom.minidom

# 取得文件完整路径
file_path = os.path.join(os.getcwd(), 'files/basic_info.xml')


def read_xml_file():
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(file_path)
    collection = DOMTree.documentElement
    print(collection)
    if collection.hasAttribute("id"):
        print("Root element : %s" % collection.getAttribute("id"))

    # 获取集合中所有记录
    record = collection.getElementsByTagName("RECORD")
    # 打印每的详细信息
    for item in record:
        print("value:{}, type:{}".format(item.getElementsByTagName('id'), type(item.getElementsByTagName('id'))))
        print("value:{}, type:{}".format(item.getElementsByTagName('id')[0], type(item.getElementsByTagName('id')[0])))
        print("value:{}, type:{}".format(item.getElementsByTagName('id')[0].childNodes, type(item.getElementsByTagName('id')[0].childNodes)))
        print("value:{}, type:{}".format(item.getElementsByTagName('id')[0].childNodes[0], type(item.getElementsByTagName('id')[0].childNodes[0])))
        print("value:{}, type:{}".format(item.getElementsByTagName('id')[0].childNodes[0].data, type(item.getElementsByTagName('id')[0].childNodes[0].data)))

        # getElementsByTagName() 方法返回带有指定名称的所有元素的 NodeList。
        # childNodes 返回文档的子节点的节点列表。
        key_id = item.getElementsByTagName('id')[0].childNodes[0].data
        print("id: {}".format(key_id))
        product_code = item.getElementsByTagName('product_code')[0].childNodes[0].data
        print("product_code: {}".format(product_code))
        full_path_id = item.getElementsByTagName('full_path_id')[0].childNodes[0].data
        print("full_path_id: {}".format(full_path_id))
        en_name = item.getElementsByTagName('en_name')[0].childNodes[0].data
        print("en_name: {}".format(en_name))
        en_full_path_name = item.getElementsByTagName('en_full_path_name')[0].childNodes[0].data
        print("en_full_path_name: {}".format(en_full_path_name))
        local_file_path = item.getElementsByTagName('local_file_path')[0].childNodes[0].data
        print("local_file_path: {}".format(local_file_path))
        modify_time_stamp = item.getElementsByTagName('modify_time_stamp')[0].childNodes[0].data
        print("modify_time_stamp: {}".format(modify_time_stamp))
        create_date = item.getElementsByTagName('create_date')[0].childNodes[0].data
        print("create_date: {}".format(create_date))

        full_path_id_str = full_path_id
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
        break


if __name__ == "__main__":
    read_xml_file()
