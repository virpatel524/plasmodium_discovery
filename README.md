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
Running meme with the following command:
#####meme ../data/ASM276v1_genes/ASM276v1_rifin.fasta -oc ../data/meme_results/ASM276_v1_rifin_10motif -maxsize 450000 -mod zoops -nmotifs 10

###2016-12-13T14:09:49
Running fimo search using the ASM276 rifin meme file, using the fimo_search script. Hopefully this will give us better matches without the NNNNN matches that we saw before.

###2016-12-13T14:21:37
Downloaded RefSeq gene seqeunces (CDS) from the following link (ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/002/765/GCA_000002765.1_ASM276v1), the previous search searched the entire genome, which obviosuly was an inefficent technique. However, it's worth considering if we would like to do a whole genome search as well? There are a considerable number of matches when we search the entire genome. Re-running FIMO using this sequence
###2016-12-13T14:30:51
Looks as though this second method is much more appropriate and functions well, producing a gff that includes each gene with the motif file we want, easily parseable. So let's make a script that can parse the gff as well as the original motif meme file, thus producing the scoring metric that we'd like.

###2016-12-13T15:50:57
First concern looking at the FIMO results is that there are a ridiculous number of false positives. First filtering approach taken was to use a q-value score of 10**-30 as a cutoff. This seems to be partially effective. Will update on how much further this goes.

Another question is whether there are domain duplicaions within the same transcript. This may suggest either poor filtering on the part of FIMO *or* is indicative of duplicated domains, of course. I will look at recovery rates using collapsed to further evaluate.

But the ambiguity here is making me a little nervous-how do we really know which matches are significant? It might be worth doing the meme approach on protein sequences and seeing whether this produces a better outcome. I'll go ahead and get this running.

###2016-12-13T16:56:43
Looking at the algorithm when we only use AAs in rifin, we get 175 matches using a pvalue cutoff of 10^-8. The next obvious test is to see if we recaptured all previous annotations using this approach. A scoring metric might also be in order for implementation, but given that we're seeing such high fidelity already, I don't think it will be necessary.

###2016-12-26T13:53:32
Read the paper describing additions to the P. vivax reference (1. Auburn,S., Böhme,U., Steinbiss,S., Trimarsanto,H., Hostetler,J., Sanders,M., Gao,Q., Nosten,F., Newbold,C.I., Berriman,M., et al. (2016) A new Plasmodium vivax reference sequence with improved assembly of the subtelomeres reveals an abundance of pir genes. Wellcome Open Res, 1, 4–9.)

I think it's very clear that there's a lot we can do with this new information. First, there's still no clear picture behind the evolutionary background of the pir genes, which could add to our understanding of the function of these genes. For instance, why are they subdivided into clusters? Does each cluster serve a unique functional purpose? Second, how does the evolutionary history of P vivax compare to Falc? If the evolutionary background of their pir genes, for instance, bears similarity, then it might suggest a  similar functional use for both. 