from math import log 
import random
import pandas as pd

random.seed(0)

def pick_kmers(s,k):
    """Input is a list of DNA sequences.
    Pick some subsequence of length k from each."""
    ret = []
    for seq in s:
        ri = random.randint(0,len(seq)-k)
        ret.append(seq[ri:ri+k])
    return ret

def prob_profile_matrix(s, laplace_rule=False):
    """Input is a list of DNA sequences of length k.
    Output a k by 4 matrix of the proportions of each
    A, C, T and G at each position.
    If laplace_rule is True, then add one to each
    base before calculating frequency."""
    n = len(s)
    k = len(s[0]) # Assuming all are same length
    mat = []
    letters = ['A','C','G','T']
    for i in range(k):
        ind_str = "".join([t[i] for t in s])
        pr = []
        for c in letters:
            # This is probably not an efficient way to do it, but whatever
            count = ind_str.count(c)
            if laplace_rule:
                pr.append((count+1)/(2*n))
            else:
                pr.append(count/n)
        mat.append(pr)
    return pd.DataFrame(mat, columns=letters)

def matrix_entropy(mat):
    """Input is the matrix from prob_profile_matrix.
    Return a list giving the entropy for each row of
    the matrix. 
    """
    return [-sum(x*log(x,2) for x in row[1]) for row in mat.iterrows()]

def most_probable_kmer(seq, k, mat):
    """Given the probability profile matrix
    and a string seq, find the substring of 
    seq of length k that has the highest 
    probability based on the matrix."""
    # Assume the sequences from which mat was derived are length k
    # Inefficient code, but who cares
    best_kmer_prob = 0
    best_kmer = ""
    for i in range(len(seq)-k):
        kmer = seq[i:i+k]
        kmer_prob = 1
        for j in range(k):
            kmer_prob *= mat.loc[j,seq[i+j]]
        if kmer_prob > best_kmer_prob:
            best_kmer_prob = kmer_prob
            best_kmer = kmer
    return best_kmer

## Driver code
seqs = [
"GTAAACAATATTTATAGC",
"AAAATTTACCTCGCAAGG",
"CCGTACTGTCAAGCGTGG",
"TGAGTAAACGACGTCCCA",
"TACTTAACACCCTGTCAA"
]

x = "TTATCCGACAGGCACGT"

k = 5

kmers = pick_kmers(seqs,5)
print(kmers)
ppm = prob_profile_matrix(kmers)
print(ppm)
ppml = prob_profile_matrix(kmers, True)
print(ppml)
print(matrix_entropy(ppml))
print(most_probable_kmer(x, k, ppml))
