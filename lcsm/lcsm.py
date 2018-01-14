"""
Finding a Shared Motif

A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of kk (k≤100k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output
AC

"""
from rosalind import read_fasta


def get_substrings(dna):
    substrings = []
    for i in range(0, len(dna) - 1):
        substring = dna[i:]
        if len(substring) > 1:
            substrings.append(substring)
        for j in range(1, len(substring) - 1):
            tiny_string = substring[0:(len(substring) - j)]
            if len(tiny_string) > 1:
                substrings.append(tiny_string)

    return sorted(substrings, key=len, reverse=True)


entries = read_fasta('rosalind_lcsm.txt')
dna = entries[0]['line']
substrings = get_substrings(dna)
print(substrings)

motif = ''
for substring in substrings:
    if motif == '':
        is_motif = True
        i = 1
        while is_motif and i < len(entries):
            if substring in entries[i]['line']:
                motif = substring
            else:
                motif = ''
                is_motif = False
            i += 1

print(motif)

outfile = open('output.txt', 'w')
outfile.write(motif)
outfile.close()
