
def get_prev_ind(curr_ind, dir):
    """
    Get the previous index tuple for the matrix based on the current index and a number
    which determines which direction to traverse (0 means diagonally up & left, 1 means
    above, 2 means left)
    """
    (i,j) = curr_ind
    if dir == 0:
        return (i-1,j-1)
    elif dir == 1:
        return (i-1,j)
    elif dir == 2:
        return (i,j-1)
    else:
        raise Exception(f"direction id '{dir}' is not valid (must be 0, 1, or 2)")

def highest_score_cell(i, j, s1, s2, mat):
    """
    Assumes 1 <= i < m, 1 <= j <= n
    """
    poss_score = [
        mat[i-1][j-1]+blosum_score(i,j,s1,s2), # from diagonal
        mat[i-1][j]+gap_penalty, # from above
        mat[i][j-1]+gap_penalty # from left
    ]
    high_score = max(poss_score)
    return (high_score, poss_score.index(high_score)) # Only returns one of the possible max values; this should be fine though

def blosum_score(i, j, s1, s2):
    """
    Only works if c1 and c2 are both valid amino acid characters.
    """
    c1, c2 = s1[i-1], s2[j-1]
    return blosum[amino_map[c1]][amino_map[c2]]

def highest_score_alignment(s1, s2):
    m, n = len(s1), len(s2)
    highest_score = 0

    mat = [[0 for j in range(n+1)] for i in range(m+1)] # used for dynamic programming
    edge_dir_list = dict() # Store the value from which the current cell value was derived

    # Filling in matrix, getting highest score
    for i in range(1,m+1):
        for j in range(1,n+1):
            prev_dir, score = highest_score_cell(i, j, s1, s2, mat)
            mat[i][j] = score
            print(f"mat[{i}][{j}] = {score}")
            edge_dir_list[(i,j)] = prev_dir # did we get to this cell from above-left, above, or left?
    print(mat)

    highest_score = mat[m][n]

    # Backtrack using edge_list to find change strings
    align1, align2 = "", ""
    curr_ind = (m,n)
    while curr_ind != (0,0):
        curr_dir = edge_dir_list[curr_ind] 
        # TODO turn the direction into useful information about what transformation occurred
        # I think the original way I did this was better actually, whoops
        curr_ind = get_prev_ind(curr_ind, curr_dir)
    return [str(highest_score), align1, align2]

def main():
    with open("./BLOSUM62.txt") as blosumin, open("./input","r") as fin, open("./output","w") as fout:
        global gap_penalty, blosum, amino_map
        s1, s2 = [line.strip() for line in fin.readlines()]
        gap_penalty = 5

        # Read in BLOSUM62 matrix
        amino_acids = blosumin.readline().split()
        amino_map = dict(zip(amino_acids, range(len(amino_acids))))
        blosum = [[int(i) for i in line.split()[1:]] for line in blosumin.readlines()]

        # Get highest alignment
        sout = highest_score_alignment(s1, s2)
        print(sout)
        fout.write("\n".join(sout))

main()