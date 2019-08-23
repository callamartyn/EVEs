#!/bin/env bash
# optspec=":q:d:o:e"
# while getopts "$optspec" option; do
# 	case "${option}" in
# 		q) query=${OPTARG};; # set minimum depth
# 		d) db=${OPTARG};; # choose a reference sequence
# 		o) output=${OPTARG};; #set number of threads
#     e) eval=${OPTARG};;
# 	esac
# done
# if [[ -z $db ]]
# then
#   db="~/db/viral/refseq/viral.protein.all.faa"
# fi
#
# # if [[ -z $output]]
# # then
# #   base=$(basename $query .fasta)
# #   output="{base}.out"
# # fi
# if [[ -z $eval ]]
# then
#   eval=1e-03
# fi
#
# echo using database $db
#
# ~/programs/ncbi-blast-2.9.0+/bin/blastx -query $query \
# -db $db -out $output  -outfmt '5' -evalue $eval
~/programs/ncbi-blast-2.9.0+/bin/blastx -query ~/EVE/data/I_scapularis/test.fasta \
-db ~/db/viral/refseq/viral.protein.all.faa -outfmt '5' -out test.out -evalue 1e-03 \
-num_threads $NSLOTS
