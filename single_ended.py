#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/22 15:10
# @Author : Yuancong Wang
# @Site : 
# @File : sing_ended.py
# @Software: PyCharm
# @E-mail: wangyuancong@163.com
'''
Description:
Output: 
Input:
Other notes:
'''


import os
import re
import subprocess




# sbtrim_path = '/home/han/opt/btrim64'  # for 86 server
btrim_path = '/home/aggl/wyc/opt/biosoft/btrim64'  # for jaas server
# btrim_path = '/home/wangyc/opt/biosoft/btrim64'  # for 87 server

wk_dir = os.getcwd()
all_files = os.listdir(wk_dir)
seq_files = [f for f in all_files if re.findall(r'.f(ast)?q(.gz)?$', f)]
print(seq_files)
print(f'find {len(seq_files)} files.')

for file in seq_files:
    in_fpath = os.path.join(wk_dir, file)
    pre_fname = re.split(r'.f(ast)?q', file)[0]
    out_fname = pre_fname + '.btrim.fq'
    out_fpath = os.path.join(wk_dir, out_fname)
    out_sum_fname = pre_fname + 'fq.sum'
    out_sum_fpath = os.path.join(wk_dir, out_sum_fname)

    cmd = f'{btrim_path} -q -t {in_fpath} -o {out_fpath} -a 20 -l 50 -s {out_sum_fpath}'
    print(f'Using btrim to process {file}...')
    if subprocess.check_call(cmd, shell=True) != 0:
        raise SystemCommandError

    print(f'Comparess {file}...')
    cmd = f'gzip {out_fpath}'
    if subprocess.check_call(cmd, shell=True) != 0:
        raise SystemCommandError

