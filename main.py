#!/usr/bin/env python
#coding:utf-8

from entry import *
from option_parser import parser
import sys

def add_bill(cost, comment):
    return add(cost, comment)

def get_bill(id):
    bill = get(id)
    print bill

def find_bill(beg, end):
    bills = find(beg, end)
    for bill in bills:
        print bill

def count_all(beg, end):
    bills = find(beg, end)
    print 'total: ', sum([b.cost for b in bills if b and b.cost])

def main():
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args(sys.argv[1:])
    if args.add:
        add_bill(float(args.add[0]), args.add[1])
    if args.list:
        find_bill(args.list[0], args.list[1])
    if args.find:
        get_bill(args.find[0])
    if args.count:
        count_all(args.list[0], args.list[1])

if __name__ == '__main__':
    main()
