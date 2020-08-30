#!/usr/bin/env python

import argparse

import op

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-op', '--op', required=True,
                        choices=['add', 'sub', 'mul', 'div'])
    parser.add_argument('-a', type=int, required=True)
    parser.add_argument('-b', type=int, required=True)

    args = parser.parse_args()

    result = None
    if args.op == 'add':
        result = op.add(args.a, args.b)
    elif args.op == 'sub':
        result = op.sub(args.a, args.b)
    elif args.op == 'mul':
        result = op.mul(args.a, args.b)
    else:
        result = op.div(args.a, args.b)

    print(f'do({args.a} {args.op} {args.b}) = {result}')
