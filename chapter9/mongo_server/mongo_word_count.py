import os
from chapter9.database.mongo_conn import get_col
from chapter9.rule import key_words
from pyecharts import Bar, Pie, WordCloud
from chapter9.config import ROOT_PATH

file_path_pre = os.path.join(ROOT_PATH, 'static/')

# 关键词统计字典
word_dict = {}


def query_from_mysql():
    """
    从表中查询结果
    :return: tuple集列表
    """
    result_list = get_col().find({}, {"_id": 0, "fen_ci_result": 1})
    return result_list


def word_count():
    word_tuple_list = query_from_mysql()
    for word_tuple in word_tuple_list:
        if word_tuple is None or len(word_tuple) <= 0:
            continue
        word_list = word_tuple.get('fen_ci_result').split(',')
        for item_val in word_list:
            if item_val is None or item_val == '' or str(item_val).strip() == '':
                continue

            # 有用字符匹配
            val_in_list = item_val in key_words.useful_word_list
            if val_in_list is False:
                continue

            count_num = word_dict.get(item_val)
            if count_num is not None and count_num >= 1:
                count_num += 1
                word_dict[item_val] = count_num
            else:
                word_dict[item_val] = 1

    draw_bar_horizontal()
    draw_pie()
    draw_word_cloud()


# 水平横条
def draw_bar_horizontal():
    word_items = list(word_dict.items())
    word_keys = [k for k, v in word_items]
    word_values = [v for k, v in word_items]
    bar = Bar('水平图表', '关键字使用情况分布')
    bar.add('引用次数', word_keys, word_values)
    # 可以选择是否在控制台打印配置信息，打开注释，执行时在控制台打印配置详情信息
    # bar.show_config()
    # html 文件存放路径
    bar.render(path=file_path_pre + "mg_bar_horizontal.html")


# 饼图
def draw_pie():
    word_items = list(word_dict.items())
    word_keys = [k for k, v in word_items]
    word_values = [v for k, v in word_items]
    pie = Pie("饼图")
    pie.add("引用次数", word_keys, word_values, is_label_show=True)
    # pie.show_config()
    # html 文件存放路径
    pie.render(path=file_path_pre + "mg_pie.html")


# 词云图
def draw_word_cloud():
    word_items = list(word_dict.items())
    word_keys = [k for k, v in word_items]
    word_values = [v for k, v in word_items]
    word_cloud = WordCloud(width=1300, height=620)
    word_cloud.add("", word_keys, word_values, word_size_range=[20, 100])
    # word_cloud.show_config()
    # html 文件存放路径
    word_cloud.render(path=file_path_pre + "mg_word_cloud.html")


if __name__ == "__main__":
    query_from_mysql()
