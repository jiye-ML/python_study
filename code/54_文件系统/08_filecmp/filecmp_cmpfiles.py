#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Compare files in two directories.
非递归比较两个目录的一组文件
"""

#end_pymotw_header
import filecmp
import os

# Determine the items that exist in both directories
d1_contents = set(os.listdir('example/dir1'))
d2_contents = set(os.listdir('example/dir2'))
common = list(d1_contents & d2_contents)
common_files = [
    f
    for f in common
    if os.path.isfile(os.path.join('example/dir1', f))
]
print('Common files:', common_files)

"""
参数：
    是目录名和两个位置上要检查的文件列表，
    传入的公共文件列表应当只包含文件名，而且这些文件在两个位置上都应当出现。

返回值：
    返回3个文件列表，分别包含匹配的文件、不匹配的文件和补鞥呢比较的文件（由于权限问题或处于其他原因）
"""
match, mismatch, errors = filecmp.cmpfiles(
    'example/dir1',
    'example/dir2',
    common_files,
)
print('Match       :', match)
print('Mismatch    :', mismatch)
print('Errors      :', errors)
