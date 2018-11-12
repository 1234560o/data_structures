# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:zwj

import argparse

parse = argparse.ArgumentParser(prog='demo', description='A demo program',
                                epilog='The end of usage')
parse.add_argument('name')
parse.add_argument('-a', '--age', type=int, required=True)
parse.add_argument('-s', '--status', choices=['alpha', 'beta', 'released'],
                   type=str, dest='myStatus')
parse.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
# parse.print_help()

args = parse.parse_args()
print(args)
