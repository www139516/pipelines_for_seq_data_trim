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

    def fit(self, path=None):
        """
        initialize the self variables in the object
        :return: self
        """
        if not path:
            self._in_path = os.getcwd()
        else:
            self._in_path = path
            self._in_path = self._get_the_abs_path()
        if os.path.isdir(self._in_path):
            self._in_dpath = self._in_path
            self._in_lst_fnames = os.listdir(self._in_dpath)
            self._in_lst_fpaths = self.get_the_fpath_lst()
        else:
            self._in_fpath = self._in_fpath
        self._get_the_paired_seq_file_path()
        return self

    def get_the_fpath_lst(self):
        lst_fpaths = []
        for fname in self._in_lst_fnames:
            fpath = os.path.join(self._in_dpath, fname)
            lst_fpaths.append(fpath)
        return lst_fpaths


    def _get_the_abs_path(self):
        return os.path.abspath(self._in_path)

    def _get_the_paired_seq_file_path(self):
        """
        serch the files in the directory, and find the paired seq files, store them to the dic
        :return: the list containing dict with paired seq files
        """
        self._in_lst_fnames.sort()
        print("Find {} files in the directory.".format(len(self._in_lst_fnames)))
        # iterate all the file names in the fname list
        for i in range(0, len(self._in_lst_fnames)-1):
            dic_pair_fname = dict()
            dic_pair_fpath = dict()
            j = i + 1
            lst_fname_i = re.split(r'_[Rr]?[12]', self._in_lst_fnames[i])
            # search the files behind the ith file, find the one match the other file of paired file[i]
            for k in range(j, len(self._in_lst_fnames)):
                lst_fname_k = re.split(r'_[Rr]?[12]', self._in_lst_fnames[k])
                if lst_fname_i == lst_fname_k:
                    dic_pair_fname['fname_r1'] = self._in_lst_fnames[i]
                    dic_pair_fname['fname_r2'] = self._in_lst_fnames[k]
                    self._in_lst_paired_fnames.append(dic_pair_fname)
                    dic_pair_fpath['fpath_r1'] = os.path.join(self._in_dpath, dic_pair_fname['fname_r1'])
                    dic_pair_fpath['fpath_r2'] = os.path.join(self._in_dpath, dic_pair_fname['fname_r2'])
                    self._in_lst_paired_fpaths.append(dic_pair_fpath)
                    break

    def get_paired_seq_fpaths(self):
        print(self._in_lst_paired_fpaths)
        print(self._in_lst_paired_fnames)
        return self._in_lst_paired_fpaths




                

