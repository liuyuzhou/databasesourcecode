"""
如示例with_theory_1.py文件中Sample类的 __exit__ 方法有三个参数 val, type 和 trace。
这些参数在异常处理中相当有用。
我们来改一下代码，看看具体如何工作的。
"""


class Sample:
    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print("type:", type)
        print("value:", value)
        print("trace:", trace)

    def do_something(self):
        bar = 1/0
        return bar + 10


with Sample() as sample:
    sample.do_something()


"""
这个例子中，with后面的get_sample()变成了Sample()。
这没有任何关系，只要紧跟with后面的语句所返回的对象有 __enter__() 和 __exit__() 方法即可。
此例中，Sample()的 __enter__() 方法返回新创建的Sample对象，并赋值给变量sample。
"""

"""
代码结果形式类似如下：
type: <class 'ZeroDivisionError'>
value: division by zero
trace: <traceback object at 0x00000000025B4908>
Traceback (most recent call last):
  File "D:/privatefile/teacher/file_read/with_theory_2.py", line 23, in <module>
    sample.do_something()
  File "D:/privatefile/teacher/file_read/with_theory_2.py", line 18, in do_something
    bar = 1/0
ZeroDivisionError: division by zero
"""

"""
实际上，在with后面的代码块抛出任何异常时，__exit__() 方法被执行。
正如例子所示，异常抛出时，与之关联的type，value和stack trace传给 __exit__() 方法，
因此抛出的ZeroDivisionError异常被打印出来了。
开发库时，清理资源，关闭文件等等操作，都可以放在 __exit__ 方法当中。

另外，__exit__ 除了用于tear things down，还可以进行异常的监控和处理，注意后几个参数。
要跳过一个异常，只需要返回该函数True即可。
"""

# 下面的样例代码跳过了所有的TypeError，而让其他异常正常抛出。
"""
def __exit__(self, type, value, traceback):
    return isinstance(value, TypeError)
"""

"""
 __exit__ 函数可以进行部分异常的处理，如果我们不在这个函数中处理异常，
 他会正常抛出，这时候我们可以这样写（python 2.7及以上版本，之前的版本参考使用contextlib.nested这个库函数）：
"""

"""
try:
    with open( "a.txt" ) as f :
        do something
except xxxError as ex:
    do something about exception
"""

"""
with-as表达式极大的简化了每次写finally的工作，这对保持代码的优雅性是有极大帮助的。
如果有多个项，我们可以这么写：
with open("x.txt") as f1, open('xxx.txt') as f2:
    do something with f1,f2
"""
