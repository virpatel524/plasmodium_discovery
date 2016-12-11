###2016-12-06T23:40:59
Opening up new repo, first implementing FIMO search.

###2016-12-07T00:02:07
Running script fimo_search, which does fimo search on default options, using the data from the meme_falc_rifin_10motif found someewhere else, will link later. Data is outputted to ../data/fimo_results/meme_falc_rifin_10motif_diana, and it is searching within the proteins found here: ~/data/cambodia_samples/falcipurum_wray/Results/Pfalciparum3D7_proteins.fasta.

###2016-12-07T00:04:14
Making some file changes to better accomadate this directory.

###2016-12-09T17:16:53
FIMO doesn't appear to be getting strong matches. Lots of Ns matched, which makes me think that these Ns are not Asp but simply reflective of unidentified regions. As such, I'm going to try running this analysis with DNA motifs. This might also save an extra step in an analysis pathway.

First step is matching Diana's rifin AA file to the genome we're using, which is easily accomplished through exonerate --model protien2genome. The results for that analyses, which used the transcripts found in the falc_from_wray directory as the target, are found in /home/vdp5/projects/plasmodium_discovery/data/exonerate_protien

###2016-12-10T15:53:30
Exonerate wasn't able to get proper matches, matching full AA seq to genomic sequences I tried. Which I think is expected because the seqeunce I matched it to was not the original. As such, I tried blasting the rifin amino acids to see what genome was closest matched so that I can use its original amino acids. However, no positive match was found. As such, I think it's smartest to go from scratch and extract the rifin genes from https://www.ncbi.nlm.nih.gov/assembly?LinkName=nuccore_assembly&from_uid=258549241, more specifically from the following page: ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/002/765/GCA_000002765.1_ASM276v1.

So with the Genbank file uploaded and placed into the data/genbank dir, ran script rifin_var_stevor.py, which parsed those sequences and turned them into nucleotide format into the directory ASM276v1_genes, with an individual file for each type.

###2016-12-11T13:27:55
Running meme with the following command: #####meme ../data/ASM276v1_genes/ASM276v1_rifin.fasta -oc ../data/meme_results/ASM276_v1_rifin_10motif -maxsize 450000 -mod zoops -nmotifs 10

