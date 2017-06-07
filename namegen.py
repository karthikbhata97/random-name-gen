#! /usr/bin/python3.5

import linecache
import random
import argparse

def maxlines():
	with open('words.txt') as f:
	    max = sum(1 for _ in f)
	return max

def getrandomline():
	line_num = random.randrange(0, max)
	line = linecache.getline('words.txt', line_num)
	line = line.split('\n')[0]
	return line

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Random filename generator!')
	parser.add_argument('--create', '-c', help='Create filename', nargs='?', const='')
	parser.add_argument('--begin', '-b', help='Begin with name', nargs='?', const='', default='')
	parser.add_argument('--end', '-e', help='End with name', nargs='?', const='', default='')
	args = parser.parse_args()
	max = maxlines()
	name = getrandomline()
	if args.create is not None:
		filename = args.begin +  name + args.end + args.create
		print("Created file: " + filename)
		with open(filename, "w") as f:
			pass
	else:
		print(name)
