
def main():
    with open("./input","r") as fin, open("./output","w") as fout:
        query = fin.readline()[:-1]
        text = fin.readline()[:-1]
        matches = []
        for i in range(len(text)-len(query)+1):
            #print(text[i:i+len(query)] + " == " + query)
            if text[i:i+len(query)] == query:
                #print(i)
                matches.append(str(i))
        fout.write(" ".join(matches))
       
if __name__ == "__main__":
    main()