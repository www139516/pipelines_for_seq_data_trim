"""
This class is used for processing files in the designated directory.
Methods:
    get_the_abs_path:
        :return the dir path or file path based on the input path
    get_the_paired_seq_file
        :return the paths of paired input file
"""

import os
import re


class FilePorcessor:

    def __init__(self):
        self._in_path = None
        self._in_dpath = None
        self._in_fpath = None
        self._in_lst_fnames = []
        self._in_lst_fpaths = []
        self._in_lst_paired_fnames = []
        self._in_lst_paired_fpaths = []
        self._out_dpath = None

    def fit(self, path=None):
        """
        initialize the self variables in the object
        :return: self
        """
        if not path:
            self._in_path = os.getcwd()
        else:
            self._in_path = path
            self._in_path = self.get_the_abs_path()
        if os.path.isdir():
            self._in_dpath = self._in_path
            self._in_lst_fnames = os.listdir(self._in_dpath)
            self._in_lst_fpaths = self.get_the_fpath_lst()
        else:
            self._in_fpath = self._in_fpath

        self._out_dpath = os.path.join(self._in_dpath, 'out')

        if not self._out_dpath:
            os.mkdir(self._out_dpath)
        self._get_the_paired_seq_file_path()

    def get_the_fpath_lst(self):
        lst_fpaths = []
        for fname in self._in_lst_fnames:
            fpath = os.path.join(self._in_dpath, fname)
            lst_fpaths.append(fpath)
        return lst_fpaths


    def get_the_abs_path(self):
        return os.path.abspath(self._in_path)

    def _get_the_paired_seq_file_path(self):
        self._in_lst_fnames.sort()
        for i in range(0, len(self._in_lst_fnames)-1):
            dic_pair_fname = dict()
            dic_pair_fpath = dict()
            j = i + 1
            pre_fname_i = re.split(r'_[Rr][12]', self._in_lst_fnames[i])[0]
            pre_fname_j = re.split(r'_[Rr][12]', self._in_lst_fnames[j])[0]
            if pre_fname_i == pre_fname_j:
                dic_pair_fname['fname_r1'] = self._in_lst_fnames[i]
                dic_pair_fname['fname_r2'] = self._in_lst_fnames[j]
                self._in_lst_paired_fnames.append(dic_pair_fname)
                dic_pair_fpath['fpath_r1'] = os.path.join(self._in_dpath, dic_pair_fname['fname_r1'])
                dic_pair_fpath['fpath_r2'] = os.path.join(self._in_dpath, dic_pair_fname['fname_r2'])
                self._in_lst_paired_fpaths.append(dic_pair_fpath)
        return self

    def print_paired_file(self):
        print(self._in_lst_paired_fpaths)
        print(self._in_lst_paired_fnames)




                

