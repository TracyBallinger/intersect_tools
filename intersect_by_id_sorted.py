#!/inside/home/common/bin/python2.7

import sys, os
import argparse

parser = argparse.ArgumentParser(description='given a file of ids and another file with a column containing those ids, it will print the subset of file1 that has the ids listed in file2. Files need to be sorted by ID.')
parser.add_argument('--col1', type=int, default=1, help= 'the column in file1 that contains the ids') 
parser.add_argument('--col2', type=int, default=1, help= 'the column in file2 that contains the ids')
parser.add_argument('-x', '--exclude', action='store_true', default=False, help= 'Using this option will print out items in file1 whose IDs are not found in file2') 
parser.add_argument('-s', '--split', nargs=2, help= 'Using this option will split file1 into two files.  split1 will have items that have ids from file2, and split2 has the rest.')
parser.add_argument('file1', help='file to extract a subset from')
parser.add_argument('file2', help= 'file containing a list of the subset of ids to extract from file1')

args=parser.parse_args()

idcolumn=args.col1 -1
id2column=args.col2 -1 
file1=open(args.file1, 'r')
file2=open(args.file2, 'r')
line1=file1.readline()
data1=line1.strip().split('\t')
id1 = data1[idcolumn]
line2=file2.readline()
data2=line2.strip().split('\t')
id2 = data2[id2column]

if args.split: 
	split_with_ids=open(args.split[0], 'w')
	split_no_ids=open(args.split[1], 'w')

looking=True
while (looking is True): 
	if (id1 == id2): 
		if args.split: 
			split_with_ids.write(line1)
		elif not args.exclude:
			sys.stdout.write(line1)
		line1=file1.readline()  
		if len(line1) != 0: #checking for the end of file1
			data1=line1.strip().split('\t')
			id1 = data1[idcolumn]
		else: 
			looking=False
	elif (id1 > id2): 
		while (id1 > id2 and looking):
			line2=file2.readline()  
			if len(line2) != 0: #checking for the end of file2
				data2=line2.strip().split('\t')
				id2 = data2[id2column]
			else: 
				looking=False
	else: # id1 < id2
		while (id1 < id2): 
			if args.split: 
				split_no_ids.write(line1)
			elif args.exclude: 
				sys.stdout.write(line1)
			line1=file1.readline()
			if len(line1) != 0: #checking for the end of file1
				data1=line1.strip().split('\t')
				id1 = data1[idcolumn]
			else: 
				looking=False
				break

while len(line1) != 0: # have not reached the end of file1
	data1=line1.strip().split('\t')
	id1 = data1[idcolumn]
	if args.split: 
		split_no_ids.write(line1)
	elif args.exclude: 
		sys.stdout.write(line1)
	line1=file1.readline()  
	 
file1.close()
file2.close()


