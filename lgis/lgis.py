"""
Longest Increasing Subsequence

A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).
A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000 followed by a permutation ππ of length nn.

Return: A longest increasing subsequence of ππ, followed by a longest decreasing subsequence of ππ.

Sample Dataset
5
5 1 4 2 3

Sample Output
1 2 3
5 4 2

"""

file = "rosalind_lgis.txt"
f = open(file, 'r')

num = int(f.readline().strip('\t\n'))
sequence = f.readline().strip('\t\n').split(' ')

inc = []
desc = []
inc_lg = "Empty"

for i in range(0, num):
    pointer = sequence[i]
    subsequences_inc = []
    for j in range(i + 1, num):
        if sequence[j] > pointer:
            subsequences_inc.append([pointer, sequence[j]])
            for subsequence_inc in subsequences_inc:
                if sequence[j] > subsequence_inc[-1]:
                    subsequence_inc.append(sequence[j])
    if len(subsequences_inc) > 0:
        subsequence_inc_longest = subsequences_inc[0]
        for subsequence_inc in subsequences_inc:
            if len(subsequence_inc) > len(subsequence_inc_longest):
                subsequence_inc_longest = subsequence_inc
        inc.append(subsequence_inc_longest)
if len(inc) > 0:
    inc_lg = inc[0]
    for subsequence in inc:
        if len(subsequence) > len(inc_lg):
            inc_lg = subsequence

print(inc_lg)
