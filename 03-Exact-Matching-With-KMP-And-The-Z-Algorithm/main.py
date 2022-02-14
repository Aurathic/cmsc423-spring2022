def main():
    with open("./input","r") as fin, open("./output","w") as fout:
        fin.readline()
        text = fin.read().replace("\n","")
        sp = [0 for x in range(len(text))]
        for i in range(1,len(text)):
            curr = sp[i-1]
            #print(f"i = {i}: {curr} > 0 and text[{i}] != text[{curr}]")
            while curr > 0 and text[i] != text[curr]:
                #print(f"{curr} > 0 and text[{i}] != text[{curr}]")
                curr = sp[curr-1]
            if text[i] == text[curr]:
                sp[i] = curr + 1
            else:
                sp[i] = 0
        #print(sp)
        fout.write(" ".join(str(x) for x in sp))

if __name__ == "__main__":
    main()
