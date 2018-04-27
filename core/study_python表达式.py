'''使用eval函数对一个字符串作为python表达式求值，可以传递一串文本，简单的表达式，或者使用内建的python函数'''def dump(expression):    result = eval(expression)    print(expression, '=>', type(result))# dump("1")# dump("1.0")# dump("'string'")# dump("1.0 + 2.0")# dump("'*' * 10")# dump("len('world')")'''如果你不确定字符串来源的安全性，那么你在使用eval的时候会遇到些麻烦，例如，某用户可能会使用__import__函数加载os模块，然后从硬盘删除文件'''print(eval('__import__("os").getcwd()'))#  这里会得到一个os.error异常，这说明python事实上在尝试删除文件！# print(eval('__import__("os").remove("file")'))# 幸运的是，这个问题很容易解决，可以给eval函数传递第二个参数，一个定义了该表达式求值时名称空间的字典，# print(eval("__import__('os').remove('file')"), {})# 这是因为python在求值前检查这个字典，如果没有发现名称为 __builtins__的变量, 它会添加一个namespace = {}# print(eval("__import__('os').remove('file')"), namespace)print(namespace.keys())# 我们注意到如果这个变量存在，python就不会去添加默认的，那么我们解决办法来了，为传递的字典参数加入一个__builtins__项即可print(eval("__import__('os').remove('file')"), {"__builtins__": {}})