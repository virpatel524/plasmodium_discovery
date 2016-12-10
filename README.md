###2016-12-06T23:40:59
Opening up new repo, first implementing FIMO search.

###2016-12-07T00:02:07
Running script fimo_search, which does fimo search on default options, using the data from the meme_falc_rifin_10motif found someewhere else, will link later. Data is outputted to ../data/fimo_results/meme_falc_rifin_10motif_diana, and it is searching within the proteins found here: ~/data/cambodia_samples/falcipurum_wray/Results/Pfalciparum3D7_proteins.fasta.

###2016-12-07T00:04:14
Making some file changes to better accomadate this directory.

###2016-12-09T17:16:53
FIMO doesn't appear to be getting strong matches. Lots of Ns matched, which makes me think that these Ns are not Asp but simply reflective of unidentified regions. As such, I'm going to try running this analysis with DNA motifs. This might also save an extra step in an analysis pathway.

First step is matching Diana's rifin AA file to the genome we're using, which is easily accomplished through exonerate --model protien2genome. The results for that analyses, which used the transcripts found in the falc_from_wray directory as the target, are found in /home/vdp5/projects/plasmodium_discovery/data/exonerate_protien_match
