with open("./input","r") as fin, open("./output","w") as fout:
    init = fin.readline()
    text = fin.read().replace("\n","")
    sp = [0 for x in range(len(text))]
    for i in range(0,len(text)-1):
        curr = sp[i]
        while curr > 0 and text[i + 1] != text[curr]:
            curr = sp[curr]
        if text[i+1] == text[curr]:
            sp[i+1] = curr + 1
        else:
            sp[i+1] = 0
    fout.write(" ".join(str(x) for x in sp))