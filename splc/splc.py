"""
RNA Splicing

After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string ss (of length at most 1 kbp) and a collection of substrings of ss acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of ss. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample Output
MVYIADKQHVASREAYGHMFKVCA
"""

from rosalind import read_fasta
from rosalind import dna_codon_table
from rosalind import output


def cut_intron(dna, intron):
    splice_dna = dna
    for i in range(0, len(dna) - len(intron)):
        if dna[i:(i + len(intron))] == intron:
            splice_dna = dna[0:i] + dna[(i + len(intron)):]

    return splice_dna


data = read_fasta("rosalind_splc.txt")

dna = data[0]['line']

for intron in data[1:]:
    dna = cut_intron(dna, intron['line'])

protein = ""
for i in range(0, len(dna), 3):
    if dna_codon_table[dna[i:(i + 3)]] != 'Stop':
        protein += dna_codon_table[dna[i:(i + 3)]]
    else:
        break

print(protein)

result = protein

output("output_splc.txt", result)



