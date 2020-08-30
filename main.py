#!/usr/bin/env python

import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-op', '--op', required=True, choices=['add', 'sub'])
	parser.add_argument('-a', type=int, required=True)
	parser.add_argument('-b', type=int, required=True)

	args = parser.parse_args()

	print(f'do({args.a} {args.op} {args.b})')
