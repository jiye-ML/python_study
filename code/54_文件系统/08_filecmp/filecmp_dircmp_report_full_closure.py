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
dc.report_full_closure()


"""
diff example/dir1 example/dir2
Only in example/dir1 : ['dir_only_in_dir1', 'file_only_in_dir1']
Only in example/dir2 : ['dir_only_in_dir2', 'file_only_in_dir2']
Identical files : ['common_file', 'contents_differ']
Common subdirectories : ['common_dir']
Common funny cases : ['file_in_dir1']

diff example/dir1\common_dir example/dir2\common_dir
Common subdirectories : ['dir1', 'dir2']

diff example/dir1\common_dir\dir1 example/dir2\common_dir\dir1
Identical files : ['common_file', 'contents_differ', 'file_in_dir1', 'file_only_in_dir1']
Common subdirectories : ['common_dir', 'dir_only_in_dir1']

diff example/dir1\common_dir\dir1\common_dir example/dir2\common_dir\dir1\common_dir

diff example/dir1\common_dir\dir1\dir_only_in_dir1 example/dir2\common_dir\dir1\dir_only_in_dir1

diff example/dir1\common_dir\dir2 example/dir2\common_dir\dir2
Identical files : ['common_file', 'contents_differ', 'file_only_in_dir2']
Common subdirectories : ['common_dir', 'dir_only_in_dir2', 'file_in_dir1']

diff example/dir1\common_dir\dir2\common_dir example/dir2\common_dir\dir2\common_dir

diff example/dir1\common_dir\dir2\dir_only_in_dir2 example/dir2\common_dir\dir2\dir_only_in_dir2

diff example/dir1\common_dir\dir2\file_in_dir1 example/dir2\common_dir\dir2\file_in_dir1
"""