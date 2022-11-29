import argparse
import os.path
import typing as tp
import re


parser = argparse.ArgumentParser(prog="mytpo",
description="This programs checks typos in given python file for comments")

parser.add_argument("filename")
parser.add_argument("-c","--correct",help="corrects typos with most likely value")

rgx_single_comment = r'#[^\n\r]+\w+(?:\*\)|[\n\r])'

# some comment

def _get_comments(file:str) -> tp.Dict:
    _comments = {}
    with open(file, "r") as f:
        _content = f.read()

    for m in re.findall(rgx_single_comment, _content):
        print(m)

    return _comments

def check_typo():

    args = parser.parse_args()
    _file = args.filename

    if not os.path.exists(_file):
        print("The file is not exist:{}".format(_file))
    else:
        _comments = _get_comments(file=_file)
        for k,v in _comments:
            print("{}:{}".format(k,v))



if __name__ == "__main__":
    check_typo()