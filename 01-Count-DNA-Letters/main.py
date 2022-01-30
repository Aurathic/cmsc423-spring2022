from collections import Counter

def main():
    with open("./input","r") as fin, open("./output","w") as fout:
        cumcount = Counter()
        for line in fin.readlines():
            cumcount.update(Counter(line))
        sout = " ".join([str(cumcount.get(let,0)) for let in list("ACGT")])
        #print(sout)
        fout.write(sout)
       
if __name__ == "__main__":
    main()