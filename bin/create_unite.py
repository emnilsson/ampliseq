#!/usr/bin/env python3
#
# Convert fasta file from UNITE into
# (i) fasta file with only sequence names and sequences
# (ii) Taxonomy file with 7 levels D_0__ to D_6__
# The files will be named db.fna and db.tax, respectively
# The contents of any files already present with those names will be overwritten.
#
# By Jeanette Tångrot 2020-09-02

#--- Import libraries, do initializations  ---#
import sys
import gzip
from Bio import SeqIO

usage = """create_unite_taxfile.py <unite.fa>
  <unite.fa> : Input. Fasta file from UNITE containing taxonomies in description line
Results will be written to two files named db.fna and db.tax. The contents of any files already present with those names will be overwritten.
"""

#--- Check and read arguments ---#
if len(sys.argv) != 2:
    exit("Usage: " + usage )

fasta_in = sys.argv[1]
fasta_out = "db.fna"
tax_out = "db.tax"

#--- Read sequence file and create new records ---#
replace_dict = {';p__': ';D_1__', ';c__': ';D_2__', ';o__': ';D_3__', ';f__': ';D_4__', ';g__': ';D_5__', ';s__': ';D_6__'}

fh_fasta = open( fasta_out, mode = 'w' )
fh_tax = open( tax_out, mode = 'w' )

with gzip.open(fasta_in, "rt") as fastafile:
    for entry in SeqIO.parse( fastafile, "fasta" ):
        (name, tax) = entry.id.split('|k__')
        tax = 'D_0__' + tax
        tax = tax.replace('unidentified','')
        for n1, n2 in replace_dict.items():
            tax = tax.replace( n1, n2 )
        tax = tax.replace('|SH','_SH')
        fh_fasta.write('>' + name + '\n' + str(entry.seq).upper() + '\n')
        fh_tax.write( name + '\t' + tax + '\n' )

fh_fasta.close()
fh_tax.close()

