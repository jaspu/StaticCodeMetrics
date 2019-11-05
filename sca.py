import subprocess
import sys
import os
import pathlib
import argparse
import json

def process_arguments():

    parser = argparse.ArgumentParser(
        description='Static Code Analysis of GH Repositories'
    )

    parser.add_argument(
        '-c',
        '--config',
        type=argparse.FileType('r'),
        default='myconfig.json',
        dest='config_file',
        help='Path to configuration file'
    )

    parser.add_argument(
        '-r',
        '--repo',
        dest='gitRepoName',
        help='Name of the repo'
    )

    if len(sys.argv) < 2:   # Here 2 means no argument, 1 argument is the program name itself
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()


def mainfunc(gitRepoAbsolutePath):
    os.chdir(gitRepoAbsolutePath)
    repoName=gitRepoAbsolutePath.split('/')[-1]
    print repoName

if __name__ == '__main__':
    args = process_arguments()
    dbConfig = json.load(args.config_file)
    gitRepoAbsolutePath = args.gitRepoName    #Name of the repo
    mainfunc(gitRepoAbsolutePath)
