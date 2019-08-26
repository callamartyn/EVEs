#!/bin/bash
bedtools getfasta -fi ../data/I_scapularis/GCA_0002086
15.1_JCVI_ISG_i3_1.0_genomic.fna -bed ./bed_files/test.bed -fo test_EVEs.fasta
