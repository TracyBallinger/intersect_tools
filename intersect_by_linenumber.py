#!/inside/home/common/bin/python2.7

import sys, os
import argparse

parser = argparse.ArgumentParser(description='will print out the lines of file1 that are indicated by number in file2.  File2 should be numerically sorted.')
parser.add_argument('--offset', type=int, default=1, help= 'if the line numbers given in file2 need to be offset by something, indicate that here.')
parser.add_argument('-x', '--exclude', action='store_true', default=False, help= 'Using this option will print out items in file1 whose line numbers are not found in file2')
parser.add_argument('-s', '--split', nargs=2, help= 'Using this option will split file1 into two files.  split1 will have file1 lines that are listed in file2, and split2 has the rest.')
parser.add_argument('file1', help='file to extract a subset from')
parser.add_argument('file2', help= 'file containing a list of the lines to extract from file1. It should be ordered.')

args=parser.parse_args()
file1=open(args.file1, 'r')
file2=open(args.file2, 'r')

if args.split:
    split_with_ids=open(args.split[0], 'w')
    split_no_ids=open(args.split[1], 'w')

linenumber=1 + args.offset
line1 = file1.readline()

for line2 in file2: 
	dat=line2.strip().split('\t')
	numkeep=int(dat[0])
	while (linenumber < numkeep): 
		if args.split: 
			split_no_ids.write(line1)
		elif args.exclude: 
			sys.stdout.write(line1)
		line1=file1.readline()
		if len(line1) != 0: #checking for end of file1
			linenumber += 1
		else: 
			sys.stderr.write("Reached end of file1")
			break
	if linenumber == numkeep: 
		if args.split: 
			split_with_ids.write(line1)
		elif not args.exclude: 
			sys.stdout.write(line1)
		line1=file1.readline()
		if len(line1) != 0: #checking for end of file1
			linenumber += 1
		else: 
			sys.stderr.write("Reached end of file1")
			break

if args.exclude or args.split:
	while len(line1) != 0: 
		if args.exclude: 
			sys.stdout.write(line1)
		elif args.split: 
			split_no_ids.write(line1)
		line1=file1.readline()

file1.close()
file2.close()


	
