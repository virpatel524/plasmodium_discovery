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

###2017-01-13T12:51:20
Looking at the characteristics of the genes that were matched. Need to extract all genes, blast/match them to the home genome, and then determine to what extent our wanted repetoire was found.

Genbank prteins for ASM276_v1 (with the  naming convention used)  are found here: /home/vdp5/projects/plasmodium_discovery/data/genbank. File obtained using the fimo_score script.

Settings used:

#####python fimo_parse_scoring.py -fimofile ../data/fimo_results/meme_falc_rifin_10motif_ASM276_v1/fimo.gff -memefile ../data/meme_results/ASM276_v1_rifin_10motif/meme.txt -genbank ../data/genbank/GCA_000002765.1_ASM276v1_genomic.gbff -genebank_name ASM276_v1

Now need to figure out how condordant the matches obtained here are with those used to train. I think the might be the same, don't remmeber entirelty.

Looking back, it's under the ASM276_v1_genes data folder, the rifins there. Since they are in another format, it will be necessary to go back and get them to better match the protein_ids found. Should be as simple as editing a script (rifin_var_stevor_ASM276v1 updated to reflect)

The intersection of the proteins identified by the FIMO approach and the known variants is 159/161, which is pretty good. It might now make sense to characteize the outliers/complements.

Majority of those not found in the other set feature the 4 domain. Notably the 4 domain is also featured in a "RIF-like gene," which supports the idea that these are accurate.

Next steps: figure out how to test the ordering of the domains found through FIMO (in what order are they featured in th genome. Best idea is to use coordinates of gene in question found in the matches.

Also important to verify if there are domain repeats. Should we also throw out overlapping matches?

Also, without a doubt, it's important to estalbish how we'll "train" search algrorithm since a manual review of all p-values is out of the question. Right now my thoughts are:
- Determine a statistical measure using a training set to see which p-values most likely correspond to matches
- Use previous p-value in the case that the value obtained is a strong enough match to use for the general case, although I kinda doubt this sadly.

Once these measures are complete, I'll want to look at the two that were excluded with rifin. They look truncated at first glance, which is encouraging in that our fundamental algorithm is not flawed. What would be of interest is determining why they did not show up–is it a p-value problem or are they fundamnetally different in temrs of sequence?

After, I think I should capture all "matches" for var, rifin, and stevor. We can determine the best phylogeny appraoch after that (especially after detemining how we're gonna establish domain sequence).
###2017-01-19T10:22:09
Running pipeline again using stevors. Using ASM276v1_stevor.fasta 

Used settings usig fimo_parse_scoring.py -memefile ../data/meme_results/ASM276v1_stevor_10motif/meme.txt -fimofile ../data/fimo_results/meme_falc_stevor_10motif/fimo.gff -genbank ../data/genbank/
ASM276_v1_proteins_by_protid.fasta     GCA_000002765.1_ASM276v1_genomic.gbff
bash-4.2$ python fimo_parse_scoring.py -memefile ../data/meme_results/ASM276v1_stevor_10motif/meme.txt -fimofile ../data/fimo_results/meme_falc_stevor_10motif/fimo.gff -genbank ../data/genbank/GCA_000002765.1_ASM276v1_genomic.gbff -output_name ASM276v1_stevor

Had match rate of 27/34, which is interesting. Possible that many undiscovered were truncated.

Working now to combine pipeline into one script, discovery_script_general.py

###2017-01-26T11:27:49
In rifin, we found that our analysis toolkit discovered several "novel" sequences containing domain 4. Looking at the original meme analysis, domain 4 looks to be a signal peptide, with variable inclusion in the rifin proteins that were annotated. 154 rifins were found to have domain 4 out of 161, which suggests that it is a highly critical motif.

I'm going to plug in a protein with domain 4 into SignalP and verify that it predicts the beginning as a signal peptide (CAG25178.1 as first test). It does whne using sensitive settings, and it's very clear. Figure titled CAG25178.1_signalP.png.

Now I'm checking protein CAG25130.1, which does not appear to have domain 4. Figure is located CAG25130.1_SignalP, and it shows that there is no signal peptide. So this shows that the signal peptide for this class of proteins is fairly conserved.

Now let's look at the composition of the proteins that matched the domain 4 requirement. How close are their domain 4s to those of the others? Are they, for instance, also signal peptides? Do they ahve other blast matches?

###2017-01-26T13:16:54
Here is my general understanding so far:

With the rifin algorithm, we found about 6 or 7 (need to look at number again) stevors included based on their signal sequences. Now since both are surface variant antigens, you'd obviously expect there to be signal sequences. What's interesting, however, is that signal sequences of protens undergoing co-antagonistic selection have undergo high rates of evolution.

So my first thought is, well, isn't the point of signal sequences to direct these proteins to the ER. Why might it matter how variable they are? And it turns out that signal peptides dictate the efficiency of translocation, which could have significant downstream effects in terms of function.

And we see that there is only ONE stevor identified which is actually in the rifin category. So to me this suggests that signal peptide evolution has led to the divergence of the two since we have been able to identify intermediates in that region.

