"""
with语句是什么?
有一些任务，可能事先需要设置，事后做清理工作。
对于这种场景，Python的with语句提供了一种非常方便的处理方式。
一个很好的例子是文件处理，你需要获取一个文件句柄，从文件中读取数据，然后关闭文件句柄。
"""

# 如果不用with语句，最原始打开方式
file = open("/tmp/foo.txt")
data = file.read()
file.close()

"""
这里有两个问题:
1. 可能忘记关闭文件句柄。
2. 文件读取数据发生异常，没有进行任何处理。
"""

# 处理异常
try:
    f = open('xxx')
except:
    print('fail to open')
    exit(-1)
try:
    # do something
    pass
except:
    # do something
    pass
finally:
     f.close()

"""
这段代码可以运行良好，但是比较冗长。
这时用with可以更优雅的来处理，with还可以很好的处理上下文环境产生的异常。
"""

# with示例
with open("/tmp/foo.txt") as file:
    data = file.read()
