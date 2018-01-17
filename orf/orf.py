"""
Open Reading Frames
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string ss of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of ss. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""

from rosalind import read_fasta
from rosalind import reverse_complement
from rosalind import dna_codon_table


def get_proteins(strand):
    proteins = []
    for i in range(0, len(strand)):
        codon = strand[i:i + 3]
        if codon == 'ATG':
            protein = "M"
            for j in range(i + 3, len(strand), 3):
                codon = strand[j:j + 3]
                if codon not in stops and len(codon) == 3:
                    protein += dna_codon_table[codon]
                else:
                    proteins.append(protein)
                    i = j + 3
                    break
    return proteins


stops = ['TAA', 'TAG', 'TGA']

entries = read_fasta('rosalind_orf.txt')
dna = entries[0]['line']
reverse_complement = reverse_complement(dna)

result = []

result.extend(get_proteins(reverse_complement))
result.extend(get_proteins(dna))

result = list(set(result))

outfile = open('output.txt', 'w')
result = '\n'.join(result)
outfile.write(result)
outfile.close()
