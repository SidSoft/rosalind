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
from math import ceil

file = "rosalind_lgis.txt"
f = open(file, 'r')

num = int(f.readline().strip('\t\n'))
sequence = f.readline().strip('\t\n').split(' ')

for i in range(0, len(sequence)):
    sequence[i] = int(sequence[i])

P = [None] * len(sequence)
M = [None] * len(sequence)
L = 1
M[0] = 0

for i in range(1, len(sequence)):
    lower = 0
    upper = L
    if sequence[M[upper - 1]] < sequence[i]:
        j = upper

    else:
        while upper - lower > 1:
            mid = (upper + lower) // 2
            if sequence[M[mid - 1]] < sequence[i]:
                lower = mid
            else:
                upper = mid

        j = lower

    P[i] = M[j - 1]

    if j == L or sequence[i] < sequence[M[j]]:
        M[j] = i
        L = max(L, j + 1)

result = []
pos = M[L - 1]
for _ in range(L):
    result.append(sequence[pos])
    pos = P[pos]

inc_lg = result[::-1]

for i in range(0, len(inc_lg)):
    inc_lg[i] = str(inc_lg[i])

print(" ".join(inc_lg))

P = [None] * len(sequence)
M = [None] * len(sequence)
L = 1
M[0] = 0

for i in range(1, len(sequence)):
    lower = 0
    upper = L
    if sequence[M[upper - 1]] > sequence[i]:
        j = upper

    else:
        while upper - lower > 1:
            mid = (upper + lower) // 2
            if sequence[M[mid - 1]] > sequence[i]:
                lower = mid
            else:
                upper = mid

        j = lower

    P[i] = M[j - 1]

    if j == L or sequence[i] > sequence[M[j]]:
        M[j] = i
        L = max(L, j + 1)

result = []
pos = M[L - 1]
for _ in range(L):
    result.append(sequence[pos])
    pos = P[pos]

desc_lg = result[::-1]

for i in range(0, len(desc_lg)):
    desc_lg[i] = str(desc_lg[i])

print(" ".join(desc_lg))

outfile = open('output.txt', 'w')
outfile.write(" ".join(inc_lg) + '\n')
outfile.write(" ".join(desc_lg))
outfile.close()
