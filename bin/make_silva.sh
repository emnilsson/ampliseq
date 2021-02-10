#!/bin/bash
#
# Unzip qiime-prepared silva-files and rename the files of interest to "db.fna" and "db.tax"
# This is for 16S-sequences and 99-dereplication

unzip -qq $1
mv SILVA_132_QIIME_release/rep_set/rep_set_16S_only/99/silva_132_99_16S.fna db.fna
mv SILVA_132_QIIME_release/taxonomy/16S_only/99/consensus_taxonomy_7_levels.txt db.tax
