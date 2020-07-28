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
        # 86 does not have fqtrim
        # self._fqtrim_path = '/home/aggl/wyc/opt/biosoft/fqtrim-0.9.7.Linux_x86_64/fqtrim'  # for jaas server
        # self._fqtrim_path = '/home/wangyc/opt/biosoft/fqtrim-0.9.7.Linux_x86_64/fqtrim'  # for 87 server


        # self._btrim_path = '/home/han/opt/btrim64'  # for 86 server
        # self._btrim_path = '/home/aggl/wyc/opt/biosoft/btrim64'  # for jaas server
        # self._btrim_path = '/home/wangyc/opt/biosoft/btrim64'  # for 87 server
        self._btrim_path = '/home/zhaohan/opt/btrim64'

        # self._paired_seq_file_path = '/public/usr/local/bin/paired_end_trim.pl'  # for jaas server
        # self._paired_seq_file_path = '/home/han/opt/paired_end_trim.pl'  # for 86 server
        # self._paired_seq_file_path = '/home/wangyc/opt/biosoft/paired_end_trim.pl' # for 87 server
        self._paired_seq_file_path = '/home/zhaohan/opt/paired_end_trim.pl'

        self._is_genome = None
        self._prefix_r1 = None
        self._prefix_r2 = None
        self._dic_btrim_out = dict()

    def fit(self, lst_paired_fpath, is_genome):
        self._is_genome = is_genome
        self._wk_dpath = os.path.dirname(lst_paired_fpath[0]['fpath_r1'])
        self._out_dpath = os.path.join(self._wk_dpath, 'out')
        if not os.path.exists(self._out_dpath):
            os.mkdir(self._out_dpath)
        for dic_path in lst_paired_fpath:
            fname1 = os.path.basename(dic_path['fpath_r1'])
            # fname2 = os.path.basename(dic_path['fpath_r2'])
            if re.findall(r'\.f(?:ast)?q\.gz$', fname1) or re.findall(r'\.f(?:ast)?q$', fname1):
                self._in_lst_fpath_1.append(dic_path['fpath_r1'])
                self._in_lst_fpath_2.append(dic_path['fpath_r2'])

    def cmd_fqtrim(self):
        if not os.path.exists(self._out_dpath):
            os.mkdir(self._out_dpath)
        assert len(self._in_lst_fpath_1) == len(self._in_lst_fpath_2), \
            "The number of R1 files must equals to the number of R2 files."
        for i in range(0, len(self._in_lst_fpath_1)):
            fpath_r1 = self._in_lst_fpath_1[i]
            fpath_r2 = self._in_lst_fpath_2[i]
            fname1 = os.path.basename(fpath_r1)
            fname2 = os.path.basename(fpath_r2)
            self._prefix_r1 = re.split(r'.f(?:ast)?q', fname1)[0]
            self._prefix_r2 = re.split(r'.f(?:ast)?q', fname2)[0]
            print('Trimming {f1} and {f2}......'.format(f1=fname1, f2=fname2))
            if self._is_genome.upper() == 'T':
                cmd = '{fqtrim} -A -l 140 -q 20 --outdir {outdir} -o trimmed.fq.gz {seq_f1},{seq_f2}'.format(
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

    def cmd_btrim(self):

        for i in range(0, len(self._in_lst_fpath_1)):
            fpath_r1 = self._in_lst_fpath_1[i]
            fpath_r2 = self._in_lst_fpath_2[i]
            fname1 = os.path.basename(fpath_r1)
            fname2 = os.path.basename(fpath_r2)
            self._prefix_r1 = re.split(r'.f(?:ast)?q', fname1)[0]
            self._prefix_r2 = re.split(r'.f(?:ast)?q', fname2)[0]
            btrim_out_fname1 = self._prefix_r1 + '.btrim.fq'
            btrim_out_fname2 = self._prefix_r2 + '.btrim.fq'
            btrim_out_fpath1 = os.path.join(self._out_dpath, btrim_out_fname1)
            btrim_out_fpath2 = os.path.join(self._out_dpath, btrim_out_fname2)

            sum_fname1 = self._prefix_r1 + '.fq.sum'
            sum_fname2 = self._prefix_r2 + '.fq.sum'
            sum_fpath1 = os.path.join(self._out_dpath, sum_fname1)
            sum_fpath2 = os.path.join(self._out_dpath, sum_fname2)
            btrim_out_sum_path1 = os.path.join(self._out_dpath, sum_fname1)
            btrim_out_sum_path2 = os.path.join(self._out_dpath, sum_fname2)

            self._dic_btrim_out = {'fpath_r1': btrim_out_fpath1,
                                   'fpath_r2': btrim_out_fpath2,
                                   'sum_fpath_r1': btrim_out_sum_path1,
                                   'sum_fpath_r2': btrim_out_sum_path2}
            cmd_btrim_r1 = '{btrim64} -q -t {in_file_path} -o {out_file_path} \
                        -a 20 -l 50 -s {sum_file}'.format(btrim64=self._btrim_path, in_file_path=fpath_r1,
                                                      out_file_path=btrim_out_fpath1,
                                                      sum_file=sum_fpath1)

            print('Using btrim to process {}...'.format(fname1))
            if subprocess.check_call(cmd_btrim_r1, shell=True) != 0:
                raise SystemCommandError

            cmd_btrim_r2 = '{btrim64} -q -t {in_file_path} -o {out_file_path} \
                        -a 20 -l 50 -s {sum_file}'.format(btrim64=self._btrim_path, in_file_path=fpath_r2,
                                                                  out_file_path=btrim_out_fpath2,
                                                                  sum_file=sum_fpath2)
            print('Using btrim to process {}...'.format(fname2))
            if subprocess.check_call(cmd_btrim_r2, shell=True) != 0:
                raise SystemCommandError

            self._cmd_paired_seq_file()
            # Remove the original fq files, Be careful.
            print(f'Removing the original fq files...{fname1}...{fname2}...')
            # os.remove(fpath_r1)
            # os.remove(fpath_r2)
        return self



    def _cmd_paired_seq_file(self):

        cmd_paired_seq = '{paired_seq_file} {sum1} {sum2} {trim1} {trim2}'.format(paired_seq_file=self._paired_seq_file_path,
                                                                                  sum1=self._dic_btrim_out['sum_fpath_r1'],
                                                                                  sum2=self._dic_btrim_out['sum_fpath_r2'],
                                                                                  trim1=self._dic_btrim_out['fpath_r1'],
                                                                                  trim2=self._dic_btrim_out['fpath_r2'])
        out_paired_fname_r1 = os.path.basename(self._dic_btrim_out['fpath_r1']) + '.pe'
        out_paired_fname_r2 = os.path.basename(self._dic_btrim_out['fpath_r2']) + '.pe'
        out_paired_fpath_r1 = os.path.join(self._out_dpath, out_paired_fname_r1)
        out_paired_fpath_r2 = os.path.join(self._out_dpath, out_paired_fname_r2)

        out_unpaired_fname_r1 = os.path.basename(self._dic_btrim_out['fpath_r1']) + '.se'
        out_unpaired_fname_r2 = os.path.basename(self._dic_btrim_out['fpath_r2']) + '.se'
        out_unpaired_fpath_r1 = os.path.join(self._out_dpath, out_unpaired_fname_r1)
        out_unpaired_fpath_r2 = os.path.join(self._out_dpath, out_unpaired_fname_r2)

        cmd_compress = 'gzip {f_r1} && gzip {f_r2}'.format(f_r1=out_paired_fpath_r1,
                                                           f_r2=out_paired_fpath_r2)

        print('Paring {f1} and {f2}...'.format(f1=os.path.basename(self._dic_btrim_out['fpath_r1']),
                                               f2=os.path.basename(self._dic_btrim_out['fpath_r2'])))
        if subprocess.check_call(cmd_paired_seq, shell=True) != 0:
            raise SystemCommandError

        print('Compressing paired files {f1} and {f2}...'.format(f1=out_paired_fname_r1,
                                                                  f2=out_paired_fname_r2))
        if subprocess.check_call(cmd_compress, shell=True) != 0:
            raise SystemCommandError

        print('Removing unnecessary files for {r1} and {r1}...'.format(r1=self._prefix_r1, r2=self._prefix_r2))
        os.remove(self._dic_btrim_out['fpath_r1'])
        os.remove(self._dic_btrim_out['fpath_r2'])
        os.remove(self._dic_btrim_out['sum_fpath_r1'])
        os.remove(self._dic_btrim_out['sum_fpath_r2'])
        os.remove(out_unpaired_fpath_r1)
        os.remove(out_unpaired_fpath_r2)
        # cmd_rm = '''
        # rm -f `ls {} | egrep -v "(pe.gz$)"`
        # '''.format(self._out_dpath)
        # if subprocess.check_call(cmd_rm, shell=True) != 0:
        #     raise SystemCommandError





