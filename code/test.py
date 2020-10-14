result = ""

def checkword(arr, w):
    for i in range(len(w), 0, -1):
        try:
            arr.index(w[:i])
        except:
            return False
    return len(w) > len(result)
    
words  = ["a","banana","app","appl","ap","apply","apple"]

words = sorted(words)
for i in range(len(words)-1):
    if(words[i] not in words[i+1]):
        if(checkword(words, words[i])):
            result = words[i]
            print result
if(checkword(words, words[-1])):
    result = words[-1]
print result