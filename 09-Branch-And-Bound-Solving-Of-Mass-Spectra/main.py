from itertools import combinations, chain
from collections import Counter

debug = False
all_amino_acids = set([57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186])

def linear_spectrum(peptide):
    masses = [sum(peptide[x:y]) for x, y in combinations(range(len(peptide)), r=2)] + [sum(peptide)]
    return Counter(masses)

def theoretical_spectrum(peptide):
    masses = [[sum(peptide[x:y]), sum(peptide[y:]+peptide[:x])] for x, y in combinations(range(len(peptide)), r=2)] + [[sum(peptide)]]
    return Counter(chain(*masses))

def possible_amino_acids(spectrum):
    return all_amino_acids.intersection(set(spectrum))

def expand(candidate_peptides, poss_amino_acids):
    return [cp + [paa] for cp in candidate_peptides for paa in poss_amino_acids]

def is_subset(a, b):
    """
    Check if one Counter is a subset of another (including multiplicities).
    """
    return len(a-b) == 0

def is_compatible(candidate_peptide, spectrum):
    return is_subset(linear_spectrum(candidate_peptide), spectrum)

def matches_spectrum(candidate_peptide, spectrum):
    return theoretical_spectrum(candidate_peptide) == spectrum

def cyclopeptide_sequences(spectrum):
    """
    Output an list of lists of number, each of which corresponds to a possible
    sequence for the cyclopeptide given the experimental spectrum. 
    """
    """
    BBCyclopeptideSequencing(S) # S is an experimental spectrum
        candidate_peptides = []
        while True
            candidate_peptides = expand(candidate_peptides) # add each potential
                                                            # letter to end of each
                                                            # peptide
            for cp in candidate_peptides
                if linear_spectrum(cp) is incompatible with S
                    remove cp from candidate_peptides
            for cp in candidate_peptides
                if theoretical_spectrum(cp) == S
                    output cp
                    remove cp from candidate_peptides
            if candidate_peptides is empty
                exit
        end while
    """
    output_peptides = []
    candidate_peptides = [[]]
    poss_amino_acids = possible_amino_acids(spectrum)
    print(poss_amino_acids)
    while candidate_peptides: # while not empty 
        candidate_peptides  = expand(candidate_peptides, poss_amino_acids)
        candidate_peptides  = [cp for cp in candidate_peptides if is_compatible(cp, spectrum)]
        output_peptides    += [cp for cp in candidate_peptides if matches_spectrum(cp, spectrum)]
        candidate_peptides  = [cp for cp in candidate_peptides if not matches_spectrum(cp, spectrum)]
        if debug:
            print(f"candidate_peptides: {candidate_peptides}")
            print(f"output_peptides: {output_peptides}")
            print("---")
    return output_peptides

# Driver Code
def main():
    with open("./input","r") as fin, open("./output","w") as fout:
        spectrum = [int(x) for x in fin.readline().split()]
        seq = cyclopeptide_sequences(Counter(spectrum))
        print(seq)
        fout.write(" ".join("-".join(seq)))

#print(theoretical_spectrum([137, 103, 147, 113]))
#print(cyclopeptide_sequences(Counter([103, 113, 137, 147, 240, 250, 250, 260, 353, 363, 387, 397, 500])))
#main()