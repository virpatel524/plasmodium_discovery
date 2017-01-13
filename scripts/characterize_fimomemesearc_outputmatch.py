import os
import csv
import sys
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument('-infile')
parser.add_argument('-compfile')
args = parser.parse_args()
args = vars(args)

infile = list(csv.reader(open(args['infile']),delimiter='\t'))
compfile = list(csv.reader(open(args['compfile']),delimiter='\t'))


inval2domain = {}

for alpha in infile:
	inval2domain[alpha[0]] = alpha[1:]


invals = [i[0] for i in infile]
compvals = [i[0].split('>')[-1] for i in compfile if '>' in i[0]]

print len(invals)
print len(compvals)


setcompval = set(compvals)
setinval = set(invals)
newdat = list(set(compvals).intersection(set(invals)))

notininval = list(setcompval.difference(setinval))
notincompval = list(setinval.difference(setcompval))

for alpha in newdat:
	if inval2domain[alpha] == ['4',]:
		print alpha

