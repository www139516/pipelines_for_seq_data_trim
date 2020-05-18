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
        self._wk_dpath = None
        self._out_dpath = None
        self._fqtrim_path = '/home/aggl/wyc/opt/biosoft/fqtrim-0.9.7.Linux_x86_64/fqtrim'
        self._is_genome = None

    def fit(self, lst_paired_fpath, is_genome):
        self._is_genome = is_genome
        self._wk_dpath = os.path.dirname(lst_paired_fpath[0]['fpath_r1'])
        self._out_dpath = os.path.join(self._wk_dpath, 'out')
        if not self._out_dpath:
            os.mkdir(self._out_dpath)
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
            if self._is_genome.upper() == 'T':
                cmd = '{fqtrim} -A -l 50 -q 20 --outdir {outdir} -o trimmed.fq.gz {seq_f1},{seq_f2}'.format(
                    fqtrim=self._fqtrim_path,
                    outdir=self._out_dpath,
                    seq_f1=fpath_r1,
                    seq_f2=fpath_r2
                )
            elif self._is_genome.upper() == 'F':
                cmd = '{fqtrim} -l 40 -q 20 --outdir {outdir} -o trimmed.fq.gz {seq_f1},{seq_f2}'.format(
                    fqtrim=self._fqtrim_path,
                    outdir=self._out_dpath,
                    seq_f1=fpath_r1,
                    seq_f2=fpath_r2
                )
            else:
                cmd = '''
                echo "Illegal input, option 'is_genome' only accept 'T' or 'F'."
                '''
            print(cmd)
            if subprocess.check_call(cmd, shell=True) != 0:
                raise SystemCommandError



