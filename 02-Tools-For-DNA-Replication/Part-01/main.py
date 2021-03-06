def match(str1, str2):
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            return False
    return True

with open("./input","r") as fin, open("./output","w") as fout:
    query = fin.readline()[:-1]
    text = fin.read().replace("\n","")
    matches = []
    for i in range(len(text)-len(query)+1):
        if match(text[i:i+len(query)],query):
            matches.append(str(i))
    fout.write(" ".join(matches))