from math import log 
import random
import pandas as pd

random.seed(0)

dna_ind_map = {"A": 0, "C": 1, "G": 2, "T": 3}

def random_kmers(s,k):
    """Input is a list of DNA sequences.
    Pick some subsequence of length k from each."""
    ret = []
    for seq in s:
        ri = random.randint(0,len(seq)-k)
        ret.append(seq[ri:ri+k])
    return ret

def first_kmers(s,k):
    return [seq[:k] for seq in s]

def prob_profile(seqs, laplace_rule=True):
    """Input is a list of DNA sequences of length k.
    Output a k by 4 matrix of the proportions of each
    A, C, T and G at each position.
    If laplace_rule is True, then add one to each
    base before calculating frequency."""
    t = len(seqs)
    k = len(seqs[0]) # Assuming all are same length
    mat = []
    letters = ['A','C','G','T']
    for i in range(k):
        ind_str = "".join([t[i] for t in seqs])
        pr = []
        for c in letters:
            # This is probably not an efficient way to do it, but whatever
            count = ind_str.count(c)
            if laplace_rule:
                pr.append((count+1)/(2*t))
            else:
                pr.append(count/t)
        mat.append(pr)
    return mat

def entropy(seqs):
    """Input is the matrix from prob_profile.
    Return the sum of the entropy for each row of
    the matrix. 
    """
    mat = prob_profile(seqs)
    return sum(-sum(x*log(x,2) for x in row) for row in mat)

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
            kmer_prob *= mat[j][dna_ind_map[seq[i+j]]]
        if kmer_prob > best_kmer_prob:
            best_kmer_prob = kmer_prob
            best_kmer = kmer
    return best_kmer

def window(s, k):
    for i in range(1 + len(s) - k):
        yield s[i:i+k]

## Driver code
"""
seqs = [
"GTAAACAATATTTATAGC",
"AAAATTTACCTCGCAAGG",
"CCGTACTGTCAAGCGTGG",
"TGAGTAAACGACGTCCCA",
"TACTTAACACCCTGTCAA"
]

x = "TTATCCGACAGGCACGT"

k = 5

kmers = pick_random_kmers(seqs,5)
print(kmers)
ppm = prob_profile_matrix(kmers, False)
print(ppm)
ppml = prob_profile_matrix(kmers, True)
print(ppml)
print(matrix_entropy(ppml))
print(most_probable_kmer(x, k, ppml))
"""

with open("./input","r") as fin, open("./output","w") as fout:
    k, t = [int(x) for x in fin.readline().split()]
    seqs = fin.readlines()
    best_motifs = first_kmers(seqs, k)
    best_entropy = entropy(best_motifs)
    for s in window(seqs[0], k):
        new_motifs = [s]
        for i in range(1,t):
            profile = prob_profile(new_motifs)
            new_motifs.append(most_probable_kmer(seqs[i], k, profile))
        new_entropy = entropy(new_motifs)
        if new_entropy < best_entropy:
            best_motifs = new_motifs
            best_entropy = new_entropy
    fout.write("\n".join(best_motifs))

# Comparing result to given answer

calculated = """ATT
AGT
ATT
ACT
ATT""".split()

given = """GAT
TAT
GAT
GAG
GAT""".split()

print(entropy(given))
print(entropy(calculated))
