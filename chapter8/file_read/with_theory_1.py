"""
with工作原理：
1、紧跟with后面的语句被求值后，返回对象的 __enter__() 方法被调用，这个方法的返回值将被赋值给as后面的变量。
2、当with后面的代码块全部被执行完之后，将调用前面返回对象的 __exit__()方法。
"""


class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        print("In __exit__()")


def get_sample():
    return Sample()


with get_sample() as sample:
    print("sample:", sample)

"""
正如我们看到的: 
1. __enter__()方法被执行。 
2. __enter__()方法返回的值 - 这个例子中是“Foo”，赋值给变量“sample”。
3. 执行代码块，打印变量“sample”的值为 “Foo”。
4. __exit__()方法被调用 with真正强大之处是它可以处理异常。
"""
