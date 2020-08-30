#!/usr/bin/env python

import argparse

import op

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-op', '--op', required=True, choices=['add', 'sub', 'mul', 'div'])
	parser.add_argument('-a', type=int, required=True)
	parser.add_argument('-b', type=int, required=True)

	args = parser.parse_args()

	func(a, b)
	result = None
	if op == 'add':
		result = op.add(a, b)
	elif op == 'sub':
		result = op.sub(a, b)
	elif op == 'mul':
		result = op.mul(a, b)
	else:
		result = op.div(a, b)

	print(f'do({args.a} {args.op} {args.b}) = {result}')

