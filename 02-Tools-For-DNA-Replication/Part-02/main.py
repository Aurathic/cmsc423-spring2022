
def main():
    with open("./input","r") as fin, open("./output","w") as fout:
        a = fin.read().replace("\n","")
        min_skew = float("inf")
        min_skew_indices = []
        skew = 0
        #print(a)
        for i in range(len(a)):
            if a[i] == "G":
                skew += 1
            elif a[i] == "C":
                skew -= 1
            if skew < min_skew:
                print("new min skew: "+ str(min_skew))
                min_skew_indices = [str(i+1)]
                min_skew = skew
            elif skew == min_skew:
                min_skew_indices.append(str(i+1))
            #print(f"{a[i]} {skew}")
        fout.write(" ".join(min_skew_indices))
        

if __name__ == "__main__":
    main()