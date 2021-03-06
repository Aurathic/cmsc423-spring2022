
def highest_score_cell(i, j, s1, s2, mat):
    """
    Assumes 1 <= i < m, 1 <= j <= n
    """
    prev_ind_score = [
        ((0,0), 0),
        ((i-1,j-1), mat[i-1][j-1]+pam_score(i,j,s1,s2)),
        ((i-1,j),   mat[i-1][j]+gap_penalty),
        ((i,j-1),   mat[i][j-1]+gap_penalty)
    ]
    #print(prev_ind_score)
    return max(prev_ind_score, key = lambda k: k[1]) # Only returns one of the possible max values; this should be fine though

def pam_score(i, j, s1, s2):
    """
    Only works if c1 and c2 are both valid amino acid characters.
    """
    c1, c2 = s1[i-1], s2[j-1]
    #print(f"{c1} {c2} -> {blosum[amino_map[c1]][amino_map[c2]]}")
    return pam[amino_map[c1]][amino_map[c2]]

def highest_score_alignment(s1, s2):
    m, n = len(s1), len(s2)
    highest_score = 0

    mat = [[0 for j in range(n+1)] for i in range(m+1)] # used for dynamic programming
    edge_list = dict()  # Store the value from which the current cell value was derived
                        # this really should be a 2d array, but whatever, this works

    # Set initial values of row and column 0
    # Set edges for row and column 0
    for i in range(1,m+1):
        #mat[i][0] = i*gap_penalty
        edge_list[(i,0)] = (0,0)
    for j in range(1,n+1):
        #mat[0][j] = j*gap_penalty
        edge_list[(0,j)] = (0,0)

    curr_ind = (m,n)
    highest_score = 0

    # Filling in matrix, getting highest score
    for i in range(1,m+1):
        for j in range(1,n+1):
            prev_ind, score = highest_score_cell(i, j, s1, s2, mat)
            mat[i][j] = score
            #print(f"mat[{i}][{j}] = {score}")
            edge_list[(i,j)] = prev_ind
            if score > highest_score:
                highest_score = score
                curr_ind = (i,j)

    # Print matrix
    [print("\t".join(str(x) for x in l)) for l in mat]

    # Backtrack using edge_list to find change strings
    align1, align2 = "", ""
    while curr_ind != (0,0):
        (i,j) = curr_ind
        #print(curr_ind)
        curr_ind = edge_list[curr_ind]
        if mat[i][j] == 0:
            break
        elif curr_ind == (i-1, j-1):
            # substitution / matching
            align1, align2 = s1[i-1] + align1, s2[j-1] + align2
        elif curr_ind == (i, j-1):
            # deletion from s1
            align1, align2 = "-" + align1, s2[j-1] + align2
        elif curr_ind == (i-1, j):
            # deletion from s2
            align1, align2 = s1[i-1] + align1, "-" + align2
        #elif curr_ind == (0,0):
        #    pass
        else:
            raise Exception(f"There's an issue with the edge list: {(i,j)} -> {curr_ind}")

    print("\n".join([align1, align2]))
    return [str(highest_score), align1, align2]

def main():
    with open("./PAM250.txt") as pamin, open("./input","r") as fin, open("./output","w") as fout:
        global gap_penalty, pam, amino_map
        s1, s2 = [line.strip() for line in fin.readlines()]
        gap_penalty = -5

        # Read in BLOSUM62 matrix
        amino_acids = pamin.readline().split()
        amino_map = dict(zip(amino_acids, range(len(amino_acids))))
        pam = [[int(i) for i in line.split()[1:]] for line in pamin.readlines()]

        #print(" ".join(amino_acids))
        #[print(" ".join(str(x) for x in l)) for l in blosum]
        
        # Get highest alignment
        sout = highest_score_alignment(s1, s2)
        print(sout)
        fout.write("\n".join(sout))

main()