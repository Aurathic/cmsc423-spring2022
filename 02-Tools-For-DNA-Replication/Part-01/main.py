with open("./input","r") as fin, open("./output","w") as fout:
    query = fin.readline()[:-1]
    text = fin.read().replace("\n","")
    matches = []
    for i in range(len(text)-len(query)+1):
        #print(text[i:i+len(query)] + " == " + query)
        if text[i:i+len(query)] == query:
            matches.append(str(i))
    fout.write(" ".join(matches))