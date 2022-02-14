import timeit 

# Copy over matching code from previous attempt, because importing is a pain
def match(str1, str2):
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            return False
    return True

def prev_match(text, pattern):
    matches = []
    for i in range(len(text)-len(pattern)+1):
        if match(text[i:i+len(pattern)],pattern):
            matches.append(str(i))
    return matches 

def sp_arr(text):
    sp = [0 for x in range(len(text))]
    for i in range(1,len(text)):
        curr = sp[i-1]
        while curr > 0 and text[i] != text[curr]:
            curr = sp[curr-1]
        if text[i] == text[curr]:
            sp[i] = curr + 1
        else:
            sp[i] = 0
    return sp

def kmp(text, pattern):
    sp = sp_arr(text)
    i = 0
    j = 0
    N = len(text)
    M = len(pattern)
    matches = []
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == M:
            matches.append(i-j)
            j = sp[j-1]
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = sp[j-1]
                i += 1


# Copied from https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
    matches = []
    # Preprocess the pattern (calculate lps[] array)
    lps = sp_arr(pat)
  
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            #print ("Found pattern at index " + str(i-j))
            matches.append(i-j)
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return matches
  
# Calculate times


with open("./input_comp.txt","r") as fin:
    pattern = fin.readline()[:-1]
    text = fin.read().replace("\n","")
    
    naive_time = timeit.timeit(lambda: prev_match(text, pattern), number=100)
    print(naive_time)
    kmp_time = timeit.timeit(lambda: KMPSearch(pattern, text), number=100)
    print(kmp_time)