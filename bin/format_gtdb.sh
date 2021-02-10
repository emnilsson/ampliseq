#!/bin/bash
#
# Convert fasta files with representative bacteria and archaea from gtdb into
# (i) fasta file with only sequence names and sequences
# (ii) Taxonomy file with 7 levels D_0__ to D_6__
# The files will be named db.fna and db.tax, respectively
# The contents of any files already present with those names will be overwritten.

tar -xOvzf $1 | cut -d ' ' -f1 > db.fna
tar -xOvzf $2 | cut -d ' ' -f1 >> db.fna

tar -xOvzf $1 | grep '^>' | sed 's/ \[.*$//' | tr -d '>' | sed -e 's/ /	/' -e 's/d__/D_0__/' -e 's/p__/D_1__/' -e 's/c__/D_2__/' -e 's/o__/D_3__/' -e 's/f__/D_4__/' -e 's/g__/D_5__/' -e 's/s__/D_6__/' -e 's/ /_/g' > db.tax
tar -xOvzf $2 | grep '^>' | sed 's/ \[.*$//' | tr -d '>' | sed -e 's/ /	/' -e 's/d__/D_0__/' -e 's/p__/D_1__/' -e 's/c__/D_2__/' -e 's/o__/D_3__/' -e 's/f__/D_4__/' -e 's/g__/D_5__/' -e 's/s__/D_6__/' -e 's/ /_/g' >> db.tax
