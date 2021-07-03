import os
from chapter9.database import models
from chapter9.rule import key_words
from pyecharts.charts import Bar, Pie, WordCloud
from pyecharts import options as opts
from chapter9.config import ROOT_PATH

file_path_pre = os.path.join(ROOT_PATH, 'static/')

# 关键词统计字典
word_dict = {}


def query_from_mysql():
    """
    从表中查询结果
    :return: tuple集列表
    """
    query_sql = "SELECT fen_ci_result FROM nlp_analysis"
    result_list = models.query_record(query_sql)
    return result_list


def word_count():
    word_tuple_list = query_from_mysql()
    for word_tuple in word_tuple_list:
        if word_tuple is None or len(word_tuple) <= 0:
            continue
        word_list = word_tuple[0].split(',')
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
    bar = Bar()
    bar.add_xaxis(word_keys)
    bar.add_yaxis('引用次数', word_values)
    bar.set_global_opts(title_opts=opts.TitleOpts(title='水平图表', subtitle='关键字使用情况分布'))
    # html 文件存放路径
    bar.render(path=file_path_pre + "bar_horizontal.html")


# 饼图
def draw_pie():
    word_items = list(word_dict.items())
    word_keys = [k for k, v in word_items]
    word_values = [v for k, v in word_items]
    data_pairs = [list(z) for z in zip(word_keys, word_values)]
    pie = Pie()
    pie.add("引用次数", data_pairs)
    pie.set_global_opts(title_opts=opts.TitleOpts(title='饼图'))
    # html 文件存放路径
    pie.render(path=file_path_pre + "pie.html")


# 词云图
def draw_word_cloud():
    word_items = list(word_dict.items())
    word_keys = [k for k, v in word_items]
    word_values = [v for k, v in word_items]
    data_pairs = [list(z) for z in zip(word_keys, word_values)]
    word_cloud = WordCloud()
    word_cloud.add("", data_pairs, word_size_range=[20, 100])
    word_cloud.set_global_opts(title_opts=opts.TitleOpts(title='词云图'))
    # html 文件存放路径
    word_cloud.render(path=file_path_pre + "word_cloud.html")


if __name__ == "__main__":
    word_count()
