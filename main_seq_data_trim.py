"""
This script is used for trimming SGS data
"""
#!/usr/bin/python
# -*- coding: <encoding name> -*-
import argparse
from processores.file_processor import FilePorcessor
from processores.cmd_processor import CmdProcessor

def fozu():
    print("                            _ooOoo_                     ")
    print("                           o8888888o                    ")
    print("                           88  .  88                    ")
    print("                           (| -_- |)                    ")
    print("                            O\\ = /O                    ")
    print("                        ____/`---'\\____                ")
    print("                      .   ' \\| |// `.                  ")
    print("                       / \\||| : |||// \\               ")
    print("                     / _||||| -:- |||||- \\             ")
    print("                       | | \\\\\\ - /// | |             ")
    print("                     | \\_| ''\\---/'' | |              ")
    print("                      \\ .-\\__ `-` ___/-. /            ")
    print("                   ___`. .' /--.--\\ `. . __            ")
    print("                ."" '< `.___\\_<|>_/___.' >'"".         ")
    print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |     ")
    print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /      ")
    print("         ======`-.____`-.___\\_____/___.-`____.-'====== ")
    print("                            `=---='  ")
    print("                                                        ")
    print("         .............................................  ")
    print("                  Prey for no bug                      ")
    print("                  Zen of python:                       ")
    print("                  Beautiful is better than ugly.；      ")
    print("                  Explicit is better than implicit.     ")
    print("                  Simple is better than complex.        ")
    print("                  Complex is better than complicated.   ")
    print("                  Flat is better than nested.           ")
    print("                  Sparse is better than dense.          ")
    print("                  Readability counts.                   ")
    print("                  Now is better than never.             ")


def main():
    fozu()
    parser = argparse.ArgumentParser(description="Trim the sequencing data in the directory.")
    parser.add_argument('-d', '--directory', help='The directory where you put the sequencing files.', default='')
    parser.add_argument('-p', '--program', help='chose the program you wang to use (btrim or fqtrim, default is btrim)',
                        default='btrim')
    parser.add_argument('-g', '--is_genome', help='"T" for sequencing data without poly A (genome sequencing data, default),\
                                                   "F" for sequencing data with poly A (transcriptome sequencing data).\
                                                  This option is only useful if you use fqtrim.',

                        default='T')
    args = parser.parse_args()
    f_proc = FilePorcessor()
    f_proc = f_proc.fit(args.directory)
    paired_seq_files = f_proc.get_paired_seq_fpaths()
    cmd_proc = CmdProcessor()
    cmd_proc.fit(paired_seq_files, args.is_genome)
    if args.program.lower() == 'btrim':
        cmd_proc.cmd_btrim()

    elif args.program.lower() == 'fqtrim':
        cmd_proc.cmd_fqtrim()
    else:
        print("Wrong program, please choose 'btrim', or 'fqtrim'.")


if __name__ == '__main__':
    main()
