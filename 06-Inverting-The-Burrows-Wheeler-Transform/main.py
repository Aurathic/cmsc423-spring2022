from itertools import chain
#https://www.geeksforgeeks.org/inverting-burrows-wheeler-transform/

def reverse_bwt(bwt):

    first_col = sorted(list(bwt))

    order_map = dict()
    order_map['$'] = []
    print(bwt)

    bwt_copy = list(bwt)
    """
    for i,c in enumerate():
        if c in order_map:
            print(f"append {i} to order_map[{c}]")
            order_map[c].append(i)
        else:
            order_map[c] = [i]
    """

    for c in first_col:
        i = bwt_copy.index(c)
        if c in order_map:
            order_map[c].append(i)
        else:
            order_map[c] = [i]
        bwt_copy[i] = '$' # TODO Really inefficient

    print(order_map)
    first_col_indexes = list(chain(*order_map.values()))
    #print(list(zip(enumerate(first_col_indexes),list(bwt))))

    ret = []
    ind = first_col_indexes[0]
    for i in range(len(bwt)):
        ind = first_col_indexes[ind]
        ret += bwt[ind]

    return "".join(ret)

def main():
    with open("./input","r") as fin, open("./output","w") as fout:
        text = fin.read().replace("\n","").strip()
        print(text)
        sout = reverse_bwt(text)
        print(sout)
        fout.write(sout)

main()

text0 = "ACTGCAG$TA"
text1 = "annb$aa"
text2 = "TTCCTAACG$A"
text3 = "AC$"
print(reverse_bwt(text0))