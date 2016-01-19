#!/inside/home/common/bin/python2.7

import sys, os
import argparse

parser = argparse.ArgumentParser(description='given a file of ids and another file with a column containing those ids, it will print the subset of file1 that has the ids listed in file2. Files do not need to be sorted by ID since the IDs in file2 are read into a hash')
parser.add_argument('-c', '--col', type=int, default=1, help= 'the column in file1 that contains the ids')
parser.add_argument('-x', '--exclude', action='store_true', default=False, help= 'Using this option will print out items in file1 whose IDs are not found in file2.')
parser.add_argument('-s', '--split', nargs=2, help= 'Using this option will split file1 into two files.  split1 will have items that have ids from file2, and split2 has the rest.')
parser.add_argument('file1', help='file to extract a subset from')
parser.add_argument('file2', help= 'file containing a list of the subset of ids to extract from file1')

args=parser.parse_args()

idcolumn=args.col -1
file1=open(args.file1, 'r')
file2=open(args.file2, 'r')

if args.split: 
	split_with_ids=open(args.split[0], 'w')
	split_no_ids=open(args.split[1], 'w')

keepids={}
for line in file2: 
	data=line.strip().split('\t')
	id2 = data[0]
	keepids[id2]=1

if args.split: 
	split_with_ids=open(args.split[0], 'w')
	split_no_ids=open(args.split[1], 'w')
	for line in file1: 
		data=line.strip().split('\t')
		id1 = data[idcolumn]
		if id1 in keepids.keys(): 
			split_with_ids.write(line)
		else: 
			split_no_ids.write(line)
elif args.exclude: 
	for line in file1: 
		data=line.strip().split('\t')
		id1 = data[idcolumn]
		if id1 not in keepids.keys(): 
			sys.stdout.write(line)
else: 
	for line in file1: 
		data=line.strip().split('\t')
		id1 = data[idcolumn]
		if id1 in keepids.keys(): 
			sys.stdout.write(line)

	

