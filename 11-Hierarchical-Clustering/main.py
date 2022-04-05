from math import sqrt
from copy import deepcopy

D_orig = None

def average_distance(cluster1, cluster2):
    """Given two clusters (lists of indices into row/columns of D), 
        calculate the average distance between the items in the cluster"""
    return sum(D_orig[i1-1][i2-1] for i1 in cluster1 for i2 in cluster2)/(len(cluster1)*len(cluster2))

def closest_clusters_indices(D, clusters):
    """Returns indices i & j into `clusters` which have lowest average distance, i < j"""
    i_out, j_out = (0, 0)
    min_dist = float("inf")
    for i in range(len(clusters)):
        for j in range(i+1,len(clusters)):
            if D[i][j] < min_dist:
                min_dist = D[i][j] 
                i_out, j_out = (i,j)
    return (i_out, j_out)

def remove_cluster_index(D, clusters, i):
    # remove row/column header
    clusters.pop(i)
    # remove row
    D.pop(i)
    #D[i] = [float("inf")] * len(D[i])
    # remove column 
    for j in range(len(D)):
        D[j].pop(i)
        #D[j][i] = float("inf")

def add_cluster(D, clusters, new_cluster):
    new_cluster_distance = [average_distance(c, new_cluster) for c in clusters]
    # add column
    for j in range(len(clusters)):
        D[j].append(new_cluster_distance[j])
    # add row
    D.append(new_cluster_distance + [0.0])
    # add row/column header
    clusters.append(new_cluster)

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
    clusters = [[i] for i in range(1,n+1)] # labels for the row/columns of distance matrix
    output = [] # each of the created clusters in order of their creation
    while len(clusters) > 1: 
        #print('\n'.join(' '.join('%2.2f' % x for x in row) for row in D))
        i, j = closest_clusters_indices(D, clusters)
        # merge ith and jth clusters
        new_cluster = clusters[i] + clusters[j]
        #print(new_cluster)
        output.append(new_cluster)
        # update the distances and clusters (row/col labels) arrays  
        add_cluster(D, clusters, new_cluster)
        remove_cluster_index(D, clusters, j)
        remove_cluster_index(D, clusters, i)
        #print(clusters)
        #print("---")
    return output

# Driver Code
def main():
    with open("./input","r") as fin, open("./output","w") as fout:
        n = int(fin.readline())
        global D_orig 
        D_orig = [list(map(float, l.split())) for l in fin.readlines()]
        out = hierarchical_clustering(deepcopy(D_orig), n)
        #print(out)
        for p in out:
            fout.write(" ".join(map(str, p)) + "\n")

main()