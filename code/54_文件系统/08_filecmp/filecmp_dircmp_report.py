#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import filecmp

dc = filecmp.dircmp('example/dir1', 'example/dir2')
dc.report()

"""
输出是一个纯文本报告，显示的结果只包含给定目录的内容，而不会递归比较其子目录。
在这里，认为文件not_the_same是相同的，因为没有办法比较内容。



diff example/dir1 example/dir2
Only in example/dir1 : ['dir_only_in_dir1', 'file_only_in_dir1']
Only in example/dir2 : ['dir_only_in_dir2', 'file_only_in_dir2']
Identical files : ['common_file', 'contents_differ']
Common subdirectories : ['common_dir']
Common funny cases : ['file_in_dir1']


"""
