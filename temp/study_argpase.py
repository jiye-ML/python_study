'''
python argparse用法总结:
    https://www.jianshu.com/p/fef2d215b91d

argparse — 命令行选项、参数和子命令的解析器:
    http://python.usyiyi.cn/translate/python_278/library/argparse.html
    
http://wiki.jikexueyuan.com/project/explore-python/Standard-Modules/argparse.html
'''

import argparse
import sys


'''
示例
'''
def example():
    '''
    $ python prog.py -h
    usage: prog.py [-h] [--sum] N [N ...]
    
    Process some integers.
    
    positional arguments:
     N           an integer for the accumulator
    
    optional arguments:
     -h, --help  show this help message and exit
     --sum       sum the integers (default: find the max)
    '''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                       const=sum, default=max, help='sum the integers (default: find the max)')
    args = parser.parse_args()
    print(args.accumulate(args.integers))

    pass


"""
argparse 使用分为三步：
1. 创建解析器(ArgumentParser对象会保存把命令行解析成Python数据类型所需要的所有信息。)
    parser = argparse.ArgumentParser(description='Process some integers.')
2. 添加参数:
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
                        help='sum the integers (default: find the max)')
    接下来，调用parse_args()返回的对象将带有两个属性，integers和accumulate。
    属性integers将是一个包含一个或多个整数的列表，
    如果命令行上指定 --sum，那么属性accumulate将是sum()函数，如果没有指定，则是max()函数。
3. 解析参数:
    parser.parse_args(['--sum', '7', '-1', '42'])
    在脚本中，parse_args() 调用一般不带参数，ArgumentParser 将根据sys.argv自动确定命令行参数。
"""


########################## 1。 ArgumentParser对象 ############################
"""
ArgumentParser对象
class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True)¶
创建一个新的ArgumentParser对象。所有的参数应该以关键字参数传递。下面有对每个参数各自详细的描述，但是简短地讲它们是：

prog - 程序的名字（默认：sys.argv[0]）(此处值为： G:/study/AI/python_study/temp/study_argpase.py)
usage - 描述程序用法的字符串（默认：从解析器的参数生成）
description - 参数帮助信息之前的文本（默认：空）
epilog - 参数帮助信息之后的文本（默认：空）
parents - ArgumentParser 对象的一个列表，这些对象的参数应该包括进去
formatter_class - 定制化帮助信息的类
prefix_chars - 可选参数的前缀字符集（默认：‘-‘）
fromfile_prefix_chars - 额外的参数应该读取的文件的前缀字符集（默认：None）
argument_default - 参数的全局默认值（默认：None）
conflict_handler - 解决冲突的可选参数的策略（通常没有必要）
add_help - 给解析器添加-h/–help 选项（默认：True）
"""


"""
parents 参数
有时候，几个解析器会共享一个共同的参数集。可以使用一个带有所有共享参数的解析器传递给
ArgumentParser的parents=参数，而不用重复定义这些参数。parents=参数接受一个ArgumentParser对象的列表，
然后收集它们当中所有的位置参数和可选参数，并将这些参数添加到正在构建的ArgumentParser对象：

>>> parent_parser = argparse.ArgumentParser(add_help=False)
>>> parent_parser.add_argument('--parent', type=int)

>>> foo_parser = argparse.ArgumentParser(parents=[parent_parser])
>>> foo_parser.add_argument('foo')
>>> foo_parser.parse_args(['--parent', '2', 'XXX'])
Namespace(foo='XXX', parent=2)

>>> bar_parser = argparse.ArgumentParser(parents=[parent_parser])
>>> bar_parser.add_argument('--bar')
>>> bar_parser.parse_args(['--bar', 'YYY'])
Namespace(bar='YYY', parent=None)

注意大部分父解析器将指定add_help=False。
否则，ArgumentParser将看到两个-h/--help 选项（一个在父解析器中，一个在子解析器中）并引发一个错误。
"""

"""
formatter_class 参数

ArgumentParser对象允许通过指定一个格式化类来定制帮助信息的格式。当前，有三个这样的类：

class argparse.RawDescriptionHelpFormatter
class argparse.RawTextHelpFormatter
class argparse.ArgumentDefaultsHelpFormatter
前两个在文本信息如何显示上允许更多控制，最后一个会自动添加关于参数默认值的信息。

默认情况下，ArgumentParser对象会对命令行帮助信息中的description和epilog文本进行换行：

>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     description='''this description
...         was indented weird
...             but that is okay''',
...     epilog='''
...             likewise for this epilog whose whitespace will
...         be cleaned up and whose words will be wrapped
...         across a couple lines''')
>>> parser.print_help()
usage: PROG [-h]

this description was indented weird but that is okay

optional arguments:
 -h, --help  show this help message and exit

likewise for this epilog whose whitespace will be cleaned up and whose words   提示： 这里换了行
will be wrapped across a couple lines

>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.RawDescriptionHelpFormatter,
...     description=textwrap.dedent('''\
...         Please do not mess up this text!
...         --------------------------------
...             I have indented it
...             exactly the way
...             I want it
...         '''))
>>> parser.print_help()
usage: PROG [-h]

Please do not mess up this text!  
--------------------------------
   I have indented it              提示： 这里没有进行自动换行操作
   exactly the way
   I want it

optional arguments:
 -h, --help  show this help message and exit
"""


########################## 2. add_argument() 方法 ############################
"""
add_argument() 方法
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
定义应该如何解析一个命令行参数。下面每个参数有它们自己详细的描述，简单地讲它们是：

name or flags - 选项字符串的名字或者列表，例如foo 或者-f, --foo。
action - 在命令行遇到该参数时采取的基本动作类型。
nargs - 应该读取的命令行参数数目。
const - 某些action和nargs选项要求的常数值。
default - 如果命令行中没有出现该参数时的默认值。
type - 命令行参数应该被转换成的类型。
choices - 参数可允许的值的一个容器。
required - 该命令行选项是否可以省略（只针对可选参数）。
help - 参数的简短描述。
metavar - 参数在帮助信息中的名字。
dest - 给parse_args()返回的对象要添加的属性名称。
"""


'''
name 或 flags 参数(当调用parse_args()时，可选的参数将以- 前缀标识，剩余的参数将被假定为位置参数：)
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-f', '--foo')
>>> parser.add_argument('bar')
>>> parser.parse_args(['BAR'])
Namespace(bar='BAR', foo=None)
>>> parser.parse_args(['BAR', '--foo', 'FOO'])
Namespace(bar='BAR', foo='FOO')
>>> parser.parse_args(['--foo', 'FOO'])
usage: PROG [-h] [-f FOO] bar
PROG: error: too few arguments
'''


'''
action 参数
ArgumentParser 对象将命令行参数和动作关联起来。
这些动作可以完成与命令行参数关联的任何事情，尽管大部分动作只是简单地给parse_args()返回的对象添加一个属性。
action 关键字参数指出应该如何处理命令行参数。支持的动作有：

1. 'store' - 只是保存参数的值。这是默认的动作。例如：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.parse_args('--foo 1'.split())
Namespace(foo='1')

2. 'append' - 保存一个列表，并将每个参数值附加在列表的后面。这对于允许指定多次的选项很有帮助。示例用法：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='append')
>>> parser.parse_args('--foo 1 --foo 2'.split())
Namespace(foo=['1', '2'])

3. 'count' - 计算关键字参数出现的次数。例如，这可用于增加详细的级别：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--verbose', '-v', action='count')
>>> parser.parse_args('-vvv'.split())
Namespace(verbose=3)

4. 你还可以通过传递一个实现了Action API的对象指定任意一个动作。实现该功能的最简单方法是扩展argparse.Action，
并提供一个合适的__call__方法。__call__方法应该接受四个参数：

parser - 包含该动作的ArgumentParser对象。
namespace - parse_args()返回的Namespace对象。大部分动作会给该对象添加一个属性。
values - 相关联的命令行参数于类型转换之后的值。（类型转换方式通过add_argument()的type关键字参数指定。）
option_string - 调用该动作的选项字符串。option_string参数是可选的，如果动作关联的位置参数将不会出现。
自定义动作的例子：

>>> class FooAction(argparse.Action):
...     def __call__(self, parser, namespace, values, option_string=None):
...         print '%r %r %r' % (namespace, values, option_string)
...         setattr(namespace, self.dest, values)
...
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action=FooAction)
>>> parser.add_argument('bar', action=FooAction)
>>> args = parser.parse_args('1 --foo 2'.split())
Namespace(bar=None, foo=None) '1' None
Namespace(bar='1', foo=None) '2' '--foo'
>>> args
Namespace(bar='1', foo='2')
'''


'''
nargs 参数
ArgumentParser对象通常将一个动作与一个命令行参数关联。
nargs关键字参数将一个动作与不同数目的命令行参数关联在一起。它支持的值有：

1. N（一个整数）。命令行中的N个参数将被一起收集在一个列表中。例如：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs=2)
>>> parser.add_argument('bar', nargs=1)
>>> parser.parse_args('c --foo a b'.split())
Namespace(bar=['c'], foo=['a', 'b'])

2. '?'。如果有的话就从命令行读取一个参数并生成一个元素。如果没有对应的命令行参数，则产生一个来自default的值。
注意，对于可选参数，有另外一种情况 - 有选项字符串但是后面没有跟随命令行参数。
在这种情况下，将生成一个来自const的值。用一些例子加以解释：
例子一：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs='?', const='c', default='d')
>>> parser.add_argument('bar', nargs='?', default='d')
>>> parser.parse_args('XX --foo YY'.split())
Namespace(bar='XX', foo='YY')
>>> parser.parse_args('XX --foo'.split())   存在可选的参数， 来自 const值
Namespace(bar='XX', foo='c')
>>> parser.parse_args(''.split())             不存在可选的参数， default
Namespace(bar='d', foo='d')

例子二
nargs='?'的一种更常见的用法是允许可选的输入和输出文件：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
...                     default=sys.stdin)
>>> parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
...                     default=sys.stdout)
>>> parser.parse_args(['input.txt', 'output.txt'])
Namespace(infile=<open file 'input.txt', mode 'r' at 0x...>,
          outfile=<open file 'output.txt', mode 'w' at 0x...>)
>>> parser.parse_args([])
Namespace(infile=<open file '<stdin>', mode 'r' at 0x...>,
          outfile=<open file '<stdout>', mode 'w' at 0x...>)

3. '*'。出现的所有命令行参数都被收集到一个列表中。
注意，一般情况下具有多个带有nargs='*'的位置参数是不合理的，但是多个带有nargs='*'的可选参数是可能的。例如：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs='*')
>>> parser.add_argument('--bar', nargs='*')
>>> parser.add_argument('baz', nargs='*')
>>> parser.parse_args('a b --foo x y --bar 1 2'.split())
Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])

4. '+'。和'*'一样，出现的所有命令行参数都被收集到一个列表中。
除此之外，如果没有至少出现一个命令行参数将会产生一个错误信息。例如：
'''

'''
default 参数
所有可选的参数以及某些位置参数可以在命令行中省略。add_argument()的default关键字参数，其默认值为None，
指出如果命令行参数没有出现时它们应该是什么值。对于可选参数，default的值用于选项字符串没有出现在命令行中的时候：

如果default的值是一个字符串，解析器将像命令行参数一样解析这个值。特别地，在设置Namespace返回值的属性之前，
解析器会调用type的转换参数。否则，解析器就使用其原始值：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('foo', nargs='?', default=42)
>>> parser.parse_args('a'.split())
Namespace(foo='a')
>>> parser.parse_args(''.split())
Namespace(foo=42)

default=argparse.SUPPRESS将导致如果没有命令行参数时不会添加属性：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default=argparse.SUPPRESS)
>>> parser.parse_args([])
Namespace()
>>> parser.parse_args(['--foo', '1'])
Namespace(foo='1')
'''

'''
required 参数
一般情况下，argparse模块假定-f和--bar标记表示可选参数，它们在命令行中可以省略。
如果要使得选项是必需的，可以指定True作为required=关键字参数的值给add_argument()：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', required=True)
>>> parser.parse_args(['--foo', 'BAR'])
Namespace(foo='BAR')
>>> parser.parse_args([])
usage: argparse.py [-h] [--foo FOO]
argparse.py: error: option --foo is required
注意 Required 选项一般情况下认为是不好的形式因为用户期望选项 是可选 的，因此应该尽可能避免这种形式。
'''

'''
help 参数
help的值是一个包含参数简短描述的字符串。当用户要求帮助时（通常通过使用-h或者--help at the command line），
这些help的描述将随每个参数一起显示出来：
>>> parser = argparse.ArgumentParser(prog='frobble')
>>> parser.add_argument('--foo', action='store_true',
...         help='foo the bars before frobbling')
>>> parser.add_argument('bar', nargs='+',
...         help='one of the bars to be frobbled')
>>> parser.parse_args('-h'.split())
usage: frobble [-h] [--foo] bar [bar ...]

positional arguments:
 bar     one of the bars to be frobbled

optional arguments:
 -h, --help  show this help message and exit
 --foo   foo the bars before frobbling
'''

'''
metavar 参数
当ArgumentParser生成帮助信息时，它需要以某种方式引用每一个参数。 
默认情况下，ArgumentParser对象使用dest的值作为每个对象的“名字”。
默认情况下，对于位置参数直接使用dest的值，对于可选参数则将dest的值变为大写。
所以，位置参数dest='bar'将引用成bar。后面带有一个命令行参数的可选参数--foo将引用成FOO。一个例子：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.add_argument('bar')
>>> parser.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
>>> parser.print_help()
usage:  [-h] [--foo FOO] bar

positional arguments:
 bar

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO
 
可以用metavar指定另外一个名字：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', metavar='YYY')
>>> parser.add_argument('bar', metavar='XXX')
>>> parser.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
>>> parser.print_help()
usage:  [-h] [--foo YYY] XXX

positional arguments:
 XXX

optional arguments:
 -h, --help  show this help message and exit
 --foo YYY
'''

'''
dest 参数
对于可选参数的动作，dest的动作通常从选项字符串推导出来。
ArgumentParser生成的dest的值是将第一长的选项字符串前面的--字符串去掉。
如果没有提供长选项字符串，dest的获得则是将第一个短选项字符串前面的-字符去掉。
任何内部的-将被转换为_字符以确保字符串是合法的属性名字。下面的实例解释了这个行为：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('-f', '--foo-bar', '--foo')
>>> parser.add_argument('-x', '-y')
>>> parser.parse_args('-f 1 -x 2'.split())
Namespace(foo_bar='1', x='2')
>>> parser.parse_args('--foo 1 -y 2'.split())
Namespace(foo_bar='1', x='2')

dest允许提供自定义的属性名：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', dest='bar')
>>> parser.parse_args('--foo XXX'.split())
Namespace(bar='XXX')
'''


################################  3. parse_args() 方法 #################
"""
ArgumentParser.parse_args(args=None, namespace=None)
将参数字符串转换成对象并设置成命名空间的属性。返回构成的命名空间。

之前对add_argument() 的调用完全决定了创建什么对象以及如何设置。详见add_argument()的文档。

默认情况下，参数字符串取自于sys.argv，并创建一个空的Namespace对象用于保存属性。
"""

'''
可选值的语法
parse_args()方法支持几种指定一个选项的值的方法。最简单的方法是，将选项和它的值以两个分开的参数传递：
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x')
>>> parser.add_argument('--foo')
>>> parser.parse_args('-x X'.split())
Namespace(foo=None, x='X')
>>> parser.parse_args('--foo FOO'.split())
Namespace(foo='FOO', x=None)
'''

'''
非法的参数
在解析命令行的同时，parse_args()会检查各种错误，
包括有歧义的选项、不合法的类型、不合法的选项、错误的位置参数个数等等。
当它遇到此类错误时，会退出并跟随用法信息一起打印出错误
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo', type=int)
>>> parser.add_argument('bar', nargs='?')

>>> # invalid type
>>> parser.parse_args(['--foo', 'spam'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: argument --foo: invalid int value: 'spam'

>>> # invalid option
>>> parser.parse_args(['--bar'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: no such option: --bar

>>> # wrong number of arguments
>>> parser.parse_args(['spam', 'badger'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: extra arguments found: badger
'''

'''
Arguments containing
parse_args()方法每当用户犯了明确的错误时会努力给出错误信息，但是有些情况天生就有歧义。
例如，命令行参数-1既可以是想指明一个选项也可以是想提供一个位置参数。
这里parse_args()会非常小心：位置参数只有在它们看上去像负数且解析器中没有选项看上去是负数时才可以以-开始：
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x')
>>> parser.add_argument('foo', nargs='?')

>>> # no negative number options, so -1 is a positional argument
>>> parser.parse_args(['-x', '-1'])
Namespace(foo=None, x='-1')

>>> # no negative number options, so -1 and -5 are positional arguments
>>> parser.parse_args(['-x', '-1', '-5'])
Namespace(foo='-5', x='-1')

>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-1', dest='one')
>>> parser.add_argument('foo', nargs='?')

>>> # negative number options present, so -1 is an option
>>> parser.parse_args(['-1', 'X'])
Namespace(foo=None, one='X')

>>> # negative number options present, so -2 is an option
>>> parser.parse_args(['-2'])
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: no such option: -2

>>> # negative number options present, so both -1s are options
>>> parser.parse_args(['-1', '-1'])
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: argument -1: expected one argument

'''


if __name__ == '__main__':

    print(sys.argv[0])

    pass
