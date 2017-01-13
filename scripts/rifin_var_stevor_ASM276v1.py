from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

output_fle_rif = open('../data/ASM276v1_genes/ASM276v1_rifin.fasta', 'w')
output_fle_var = open('../data/ASM276v1_genes/ASM276v1_var.fasta', 'w')
output_fle_stevor = open('../data/ASM276v1_genes/ASM276v1_stevor.fasta', 'w')

output_fle_rif_protein = open(
    '../data/ASM276v1_genes/ASM276v1_rifin_prot.fasta', 'w')
output_fle_var_protein = open(
    '../data/ASM276v1_genes/ASM276v1_var_prot.fasta', 'w')
output_fle_stevor_protein = open(
    '../data/ASM276v1_genes/ASM276v1_stevor_prot.fasta', 'w')

allrecs = list(SeqIO.parse(
    open('../data/genbank/GCA_000002765.1_ASM276v1_genomic.gbff', "r"), "genbank"))


for data in allrecs:
    for alpha in data.features:
        if alpha.type != 'CDS': continue
        tmp = alpha.qualifiers
        if 'product' in tmp:
            if 'rifin' in tmp['product'][0]:
                sequence = alpha.extract(data.seq)
                seqob = sequence
                if 'pseudo' in tmp:
                    output_fle_rif.write(
                        '>%s\n' % (tmp['locus_tag'][0]))
                    output_fle_rif_protein.write(
                        '>%s\n' % (tmp['locus_tag'][0]))
                    output_fle_rif.write('%s\n' % (sequence))
                    output_fle_rif_protein.write('%s\n' % (seqob.translate()))
                else:
                    output_fle_rif.write(
                        '>%s\n' % (tmp['protein_id'][0]))
                    output_fle_rif_protein.write(
                        '>%s\n' % (tmp['protein_id'][0]))
                    output_fle_rif.write('%s\n' % (sequence))
                    output_fle_rif_protein.write('%s\n' % (seqob.translate()))

            if 'var' in tmp['product'][0]:
                sequence = alpha.extract(data.seq)
                seqob = sequence
                if 'pseudo' in tmp:
                    output_fle_var.write(
                        '>%s\n' % (tmp['locus_tag'][0]))
                    output_fle_var_protein.write(
                        '>%s\n' % (tmp['locus_tag'][0]))
                    output_fle_var.write('%s\n' % (sequence))
                    output_fle_var_protein.write('%s\n' % (seqob.translate()))
                else:
                    output_fle_var.write(
                        '>%s\n' % (tmp['protein_id'][0]))
                    output_fle_var_protein.write(
                        '>%s\n' % (tmp['protein_id'][0]))
                    output_fle_var.write('%s\n' % (sequence))
                    output_fle_var_protein.write('%s\n' % (seqob.translate()))

            if 'stevor' in tmp['product'][0]:
                sequence = alpha.extract(data.seq)
                seqob = sequence
                if 'pseudo' in tmp:
                    output_fle_stevor.write(
                        '>%s\n' % (tmp['locus_tag'][0]))
                    output_fle_stevor_protein.write(
                        '>%s\n' % (tmp['locus_tag'][0]))
                    output_fle_stevor.write('%s\n' % (sequence))
                    output_fle_stevor_protein.write('%s\n' % (seqob.translate()))
                else:
                    output_fle_stevor.write(
                        '>%s\n' % (tmp['protein_id'][0]))
                    output_fle_stevor_protein.write(
                        '>%s\n' % (tmp['protein_id'][0]))
                    output_fle_stevor.write('%s\n' % (sequence))
                    output_fle_stevor_protein.write('%s\n' % (seqob.translate()))

output_fle_rif.close()
output_fle_stevor.close()
output_fle_var.close()
