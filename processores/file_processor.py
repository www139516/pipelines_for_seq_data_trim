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

    def get_the_fpath_lst(self):
        lst_fpaths = []
        for fname in self._in_lst_fnames:
            fpath = os.path.join(self._in_dpath, fname)
            lst_fpaths.append(fpath)
        return lst_fpaths


    def get_the_abs_path(self):
        return os.path.abspath(self._in_path)

    def get_the_paired_seq_file_path(self):
        lst_fname_r1 = []
        lst_fname_r2 = []
        pat = '_R2'
        for fname_r2 in self._in_lst_fnames:
            upper_name = fname_r2.upper()
            if pat in upper_name:
                lst_fname_r2.append(fname_r2)
        for fname in lst_fname_r2:
            fname_pre = re.split(r'_[Rr]2', fname)[0]
            for fname in self._in_lst_fnames:
                

