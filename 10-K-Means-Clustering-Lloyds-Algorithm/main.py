debug = True

def centroid(points):
    n = len(points)
    return tuple(sum(ds)/n for ds in zip(*points))

def squared_distance(p1, p2):
    return sum((d1-d2)**2 for d1, d2 in zip(p1,p2))

def closest_point(points, p):
    """Return point in points which is closest to p."""
    return min(points, key=lambda px: squared_distance(px, p))

def lloyd(k, m, points):
    centers_old = []
    centers = points[:k]
    while sorted(centers_old) != sorted(centers):
        centers_old = centers.copy()
        clusters = [[] for i in range(k)]
        # Partition points by their closest point in center
        for p in points:
            clusters[centers.index(closest_point(centers, p))].append(p)
        # Find new centers of clusters
        for i,c in enumerate(clusters):
            centers[i] = centroid(c)
    return centers

# Driver Code
def main():
    with open("./input","r") as fin, open("./output","w") as fout:
        k, m = map(int, fin.readline().split())
        points = [tuple(map(float, l.split())) for l in fin.readlines()]
        out = lloyd(k, m, points)
        print(out)
        for p in out:
            fout.write(" ".join(map(str, p)) + "\n")

main()