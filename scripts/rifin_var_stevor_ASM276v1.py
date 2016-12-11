from Bio import SeqIO

output_fle_rif = open('../data/ASM276v1_genes/ASM276v1_rifin.fasta', 'w')
output_fle_var = open('../data/ASM276v1_genes/ASM276v1_var.fasta', 'w')
output_fle_stevor = open('../data/ASM276v1_genes/ASM276v1_stevor.fasta', 'w')

allrecs = list(SeqIO.parse(
    open('../data/genbank/GCA_000002765.1_ASM276v1_genomic.gbff', "r"), "genbank"))


for data in allrecs:
    for alpha in data.features:
        tmp = alpha.qualifiers
        if 'product' in tmp:
            if 'rifin' in tmp['product'][0]:
                sequence = alpha.extract(data.seq)
                output_fle_rif.write(
                    '>%s\n' % (tmp['locus_tag'][0]))
                output_fle_rif.write('%s\n' % (sequence))

            if 'var' in tmp['product'][0]:
                sequence = alpha.extract(data.seq)
                output_fle_var.write(
                    '>%s\n' % (tmp['locus_tag'][0]))
                output_fle_var.write('%s\n' % (sequence))

            if 'stevor' in tmp['product'][0]:
                sequence = alpha.extract(data.seq)
                output_fle_stevor.write(
                    '>%s\n' % (tmp['locus_tag'][0]))
                output_fle_stevor.write('%s\n' % (sequence))

output_fle_rif.close()
output_fle_stevor.close()
output_fle_var.close()
