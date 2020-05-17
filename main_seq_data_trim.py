"""
This script is used for trimming SGS data
"""
import argparse
from processores.file_processor import FilePorcessor
from processores.cmd_processor import CmdProcessor


def main():
    parser = argparse.ArgumentParser(description="Trim the sequencing data in the directory.")
    parser.add_argument('-d', '--directory', help='The directory where you put the sequencing files.', default='')
    args = parser.parse_args()
    f_proc = FilePorcessor()
    f_proc = f_proc.fit(args.directory)
    paired_seq_files = f_proc.get_paired_seq_fpaths()
    cmd_proc = CmdProcessor()
    cmd_proc.fit(paired_seq_files)
    cmd_proc.cmd_trim()




if __name__ == '__main__':
    main()
