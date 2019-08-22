#!/bin/env bash
~/programs/ncbi-blast-2.9.0+/bin/blastx -query ./data/BulkLib1_S1_R1_001.fasta \
-db ~/db/piwi/PF02171_full_length_sequences.fasta -out ./out/BulkLib1_R1_piwi_1e-05.blastx.tsv -outfmt '7' -evalue 1e-05
