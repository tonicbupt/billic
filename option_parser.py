#!/usr/bin/env python
# coding: utf-8

import argparse


parser = argparse.ArgumentParser(description='bill')
parser.add_argument('-add', nargs=2, help='增加新条目, -add cost comment')
parser.add_argument('-list', nargs=2, help='查询条目, -list beg end')
parser.add_argument('-find', nargs=1, help='查询条目, -find id')

