"""
This script is used for processing the cmd (like btrim)
"""

import subprocess
import os
import re


class CmdProcessor:

    def __init__(self):
        self._in_lst_fpath_1 = []
        self._in_lst_fpath_2 = []
        self._wk_dpath = os.getcwd()
        self._out_dpath = os.path.join(self._wk_dpath, 'out')

    def fit(self, lst_paired_fpath):
        for dic_path in lst_paired_fpath:
            fname1 = os.path.basename(dic_path['fpath_r1'])
            if re.findall(r'\.f(?:ast)?q\.gz$', fname1) or re.findall(r'\.f(?:ast)?q$', fname1):
                self._in_lst_fpath_1.append(dic_path['fpath_r1'])
                self._in_lst_fpath_2.append(dic_path['fpath_r2'])

    def cmd_trim(self):
        if not os.path.exists(self._out_dpath):
            os.mkdir(self._out_dpath)
        assert len(self._in_lst_fpath_1) == len(self._in_lst_fpath_2), \
            "The number of R1 files must equals to the number of R2 files."
        for i in range(0, len(self._in_lst_fpath_1)):
            fpath_r1 = self._in_lst_fpath_1[i]
            fpath_r2 = self._in_lst_fpath_2[i]
            fname1 = os.path.basename(fpath_r1)
            fname2 = os.path.basename(fpath_r2)
            print('Trimming {f1} and {f2}......'.format(f1=fname1, f2=fname2))
            cmd = ''



