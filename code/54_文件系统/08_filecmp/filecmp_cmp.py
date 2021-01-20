#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Compare two files.
"""

#end_pymotw_header
import filecmp


""" 
shallow 参数告诉cmp（）除了文件的元数据外，是否还要查看文件的内容，默认情况下，会使用os.stat（）得到的信息来完成比较，
    如果是一样的，则认为相同，
因此，对于同事创建的相同大小的文件，即使他们内容不同，也会报告认为是相同的文件。当shallow为False时，则要比较文件的内容。 
"""
print('common_file    :', end=' ')
print(filecmp.cmp('example/dir1/common_file',
                  'example/dir2/common_file',
                  shallow=True),
      end=' ')
print(filecmp.cmp('example/dir1/common_file',
                  'example/dir2/common_file',
                  shallow=False))

print('contents_differ:', end=' ')
print(filecmp.cmp('example/dir1/contents_differ',
                  'example/dir2/contents_differ',
                  shallow=True),
      end=' ')
print(filecmp.cmp('example/dir1/contents_differ',
                  'example/dir2/contents_differ',
                  shallow=False))

print('identical      :', end=' ')
print(filecmp.cmp('example/dir1/file_only_in_dir1',
                  'example/dir1/file_only_in_dir1',
                  shallow=True),
      end=' ')
print(filecmp.cmp('example/dir1/file_only_in_dir1',
                  'example/dir1/file_only_in_dir1',
                  shallow=False))
