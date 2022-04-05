from math import sqrt
debug = True

def average_distance(D, cluster1, cluster2):
    """Given two clusters (lists of indices into row/columns of D), 
        calculate the average distance between the items in the cluster"""
    return sum(D[i1][i2] for i1 in cluster1 for i2 in cluster2)/(len(cluster1)*len(cluster2))

def closest_clusters_indices(D, clusters):
    """Returns indices i & j into `clusters` which have lowest average distance, i < j"""
    i_out, j_out = (0, 0)
    min_dist = float("inf")
    for i in range(len(clusters)):
        for j in range(i,len(clusters)):
            dist = average_distance(D, clusters[i], clusters[j])
            if dist < min_dist:
                min_dist = dist 
                i_out, j_out = (i,j)
    return (i_out, j_out)

def remove_cluster(D, i):
    # remove row
    D[i] = [float("inf")] * len(D[i])
    # remove column 
    for j in range(len(D)):
        D[j][i] = float("inf")

def remove_clusters(D, ind_list):
    for i in ind_list:
        remove_cluster(D, i)

def add_cluster(D, cluster):
    pass

def hierarchical_clustering(D, n):
    """HierarchicalClustering(D, n)
    Clusters ← n single-element clusters labeled 1, ... , n
    construct a graph T with n isolated nodes labeled by single elements 1, ... , n
    while there is more than one cluster 
        find the two closest clusters Ci and Cj 
        merge Ci and Cj into a new cluster Cnew with |Ci| + |Cj| elements
        add a new node labeled by cluster Cnew to T
        connect node Cnew to Ci and Cj by directed edges
        remove the rows and columns of D corresponding to Ci and Cj
        remove Ci and Cj from Clusters
        add a row/column to D for Cnew by computing D(Cnew, C) for each C in Clusters
        add Cnew to Clusters 
    assign root in T as a node with no incoming edges
    return T"""
    clusters = [[i] for i in range(n)] # labels for the row/columns of distance matrix
    output = []
    while len(clusters) > 1: 
        i, j = closest_clusters_indices(clusters)

        # merge ith and jth clusters
        c_new = clusters[i] + clusters[j]
        output.append(c_new)
        clusters.append(c_new)

        # remove merged clusters
        # TODO

    return output

# Driver Code
def main():
    with open("./input","r") as fin, open("./output","w") as fout:
        n = int(fin.readline().split())
        dist_mat = [tuple(map(float, l.split())) for l in fin.readlines()]
        out = hierarchical_clustering(dist_mat, n)
        print(out)
        for p in out:
            fout.write(" ".join(map(str, p)) + "\n")

main()