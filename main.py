#!/usr/bin/env python

import argparse
import op


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-op', '--op', required=True,
                        choices=['add', 'sub', 'mul', 'div'])
    parser.add_argument('-a', type=int, required=True)
    parser.add_argument('-b', type=int, required=True)

    args = parser.parse_args()
    return args.op, args.a, args.b


def main(oper=None, a=0, b=0):
    if not(all([oper, a, b])):
        oper, a, b = parse_args()
    result = None
    if oper == 'add':
        result = op.add(a, b)
    elif oper == 'sub':
        result = op.sub(a, b)
    elif oper == 'mul':
        result = op.mul(a, b)
    else:
        result = op.div(a, b)

    print(f'do({a} {oper} {b}) = {result}')


if __name__ == '__main__':
    main()
