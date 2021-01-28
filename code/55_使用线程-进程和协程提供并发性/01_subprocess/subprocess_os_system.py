#!/usr/bin/env python3
"""Replacing os.system with subprocess.
"""

#end_pymotw_header
import subprocess


"""
命令行参数作为一个字符串列表传入，这样无须对引号或其他可能由shell解释的特殊字符转义，
run（）返回一个CompletedProcess实例，它包含进程的有关信息，如退出的码和输出。
"""
completed = subprocess.run(['ls', '-1'])
print('returncode:', completed.returncode)
