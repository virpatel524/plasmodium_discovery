import os
import csv
import sys
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument('-memefile')
parser.add_argument('-fimofile')
parser.add_argument('-genbank')
parser.add_argument('-genebank_name')
args = parser.parse_args()
args = vars(args)

memefle = list(csv.reader(open(args['memefile']), delimiter='\t'))
fimofle = list(csv.reader(open(args['fimofile']), delimiter='\t'))
genbank =  args['genbank']
gbname = args['genebank_name']
totalmotifnum = 0
motif2num = {}

gene2motifs = {}

counter = 1
for alpha in memefle:
    if len(alpha) == 0:
        continue
    # print alpha
    if alpha[0][:4] == 'data':
        beta = [a for a in alpha[0].split(' ') if a != '']
        totalmotifnum = float(beta[4])

    if alpha[0][:2] == 'BL':
        zeta = float(
            [a for a in alpha[0].split(' ') if a != ''][-1].split('=')[-1])
        motif2num[str(counter)] = zeta
        counter += 1

# use fimo gff file here

for alpha in fimofle:
    if '##' in alpha[0]:
        continue
    genename = alpha[0]
    num = alpha[-1].split(';')[0].split('=')[-1]
    pvalue = float(alpha[-1].split(';')[3].split('=')[-1])
    if pvalue < 10.0**(-8):
        gene2motifs.setdefault(genename, []).append(num)


output = open('../data/genbank/{}_proteins_by_protid.fasta'.format(gbname), 'w')

for seq_record in SeqIO.parse(genbank, 'genbank'):
    for zeta  in seq_record.features:
        if zeta.type  == 'CDS':
            if 'protein_id' in zeta.qualifiers:
                output.write('> {}\n'.format(zeta.qualifiers['protein_id'][0]))
                output.write('{}\n'.format(zeta.qualifiers['translation'][0]))




