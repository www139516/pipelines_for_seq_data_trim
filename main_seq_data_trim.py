"""
This script is used for trimming SGS data
"""
import argparse
from processores.file_processor import FilePorcessor


def main():
    parser = argparse.ArgumentParser(description="Trim the sequencing data in the directory.")
    parser.add_argument('-d', '--directory', help='The directory where you put the sequencing files.', default='')
    args = parser.parse_args()
    f_proc = FilePorcessor()
    f_proc.fit(args.directory)
    f_proc.print_paired_file()




if __name__ == '__main__':
    main()
