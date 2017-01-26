import sys
import csv
import argparse 
import subprocess
from subprocess import Popen

parser = argparse.ArgumentParser()
parser.add_argument('-protein_file')
parser.add_argument('-search_set')
parser.add_argument('-outname')
parser.add_argument('-genbank')
# parser.add_argument('genebank_name')
args = parser.parse_args()
args = vars(args)

protfile = args['protein_file']
finname = args['outname']
searchset = args['search_set']
genbank =  args['genbank']
# gbname = args['genebank_name']

memecommand = 'meme {} -oc ../data/meme_results/{}_meme -maxsize 450000 -mod zoops -nmotifs 10 -p 4'.format(protfile, finname )
print memecommand
com = Popen(memecommand, shell=True, stdout=subprocess.PIPE)
com.wait()
print 'vir'

fimocommand = 'fimo -oc {} {} {}'.format('../data/fimo_results/{}_fimo'.format(finname),'../data/meme_results/{}_meme/meme.txt'.format(finname), searchset)
com = Popen(fimocommand, shell=True, stdout=subprocess.PIPE)
com.wait()

memefle = list(csv.reader(open('../data/meme_results/{}_meme/meme.txt'.format(finname)), delimiter='\t'))
fimofle = list(csv.reader(open('../data/fimo_results/{}_fimo/fimo.gff'.format(finname)), delimiter='\t'))
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


# output = open('../data/genbank/{}_proteins_by_protid.fasta'.format(gbname), 'w')

# for seq_record in SeqIO.parse(genbank, 'genbank'):
#     for zeta  in seq_record.features:
#         if zeta.type  == 'CDS':
#             if 'protein_id' in zeta.qualifiers:
#                 output.write('>{}\n'.format(zeta.qualifiers['protein_id'][0]))
#                 output.write('{}\n'.format(zeta.qualifiers['translation'][0]))
# output.close()


output = open('../data/fimo_meme_searchoutput/{}.txt'.format(finname), 'w')


for alpha in gene2motifs:
    output.write('{}\t'.format(alpha))
    output.write('\t'.join(gene2motifs[alpha]) + '\n')

infile = list(csv.reader(open('../data/fimo_meme_searchoutput/{}.txt'.format(finname)),delimiter='\t'))
compfile = list(csv.reader(open(protfile),delimiter='\t'))


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
