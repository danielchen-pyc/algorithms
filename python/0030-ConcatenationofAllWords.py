'''
You are given a string s and an array of strings words of the same length. Return
all starting indices of substring(s) in s that is a concatenation of each word in
words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.
'''



# My Solution (Runtime 10.27%, Memory 93.63%)
def findSubstring(self, s: str, words: List[str]) -> List[int]:
    if not words or s == "":
        return []
    i = 0
    wlen = len(words[0])
    d = {}
    answer = []
    while i < len(s):
        currword = s[i:i+wlen]
        wordNum = words.count(currword)
        if wordNum == 0 and d:
            i -= wlen*(sum(d.values()))-1
            d = {}
            currword = s[i:i+wlen]
            wordNum = words.count(currword)
        while wordNum == 0 and i <= len(s)-len(words)*wlen:
            i += 1
            currword = s[i:i+wlen]
            wordNum = words.count(currword)
        if currword not in words:
            i += 1
            continue
        if currword not in d:
            d[currword] = 1
            if sum(d.values()) == len(words):
                answer.append(i-wlen*(len(words)-1))
                i -= wlen*(len(words)-1)-1
                d = {}
            else:
                i += wlen
        elif currword in d and d[currword] < wordNum:
            d[currword] += 1
            if sum(d.values()) == len(words):
                answer.append(i-wlen*(len(words)-1))
                i -= wlen*(len(words)-1)-1
                d = {}
            else:
                i += wlen
        else:
            i -= wlen*(sum(d.values()))-1
            d = {}
    return answer



# Other Solution (Runtime 75.41%)
def findSubstring(self, s: str, words: List[str]) -> List[int]:
    if not s or not words or not words[0]:
        return []

    S: int = len(s)
    W: int = len(words)
    L: int = len(words[0])

    wordCounts: Dict[str, int] = defaultdict(int)
    for word in words:
        wordCounts[word] += 1

    def concatStartsAt(concatStart: int) -> bool:
        wordCountsCopy: Dict[str, int] = wordCounts.copy()

        for iW in range(W):
            wordStart: int = concatStart + iW * L
            word: str = s[wordStart : wordStart + L]

            if not wordCountsCopy[word]:
                return False
            wordCountsCopy[word] -= 1

        return True

    return [iS for iS in range(S - W * L + 1) if concatStartsAt(iS)]




# Other Solution (75ms)
def findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if not s or words==[]:
        return []
    lenstr=len(s)
    lenword=len(words[0])
    lensubstr=len(words)*lenword
    times={}
    for word in words:
        if word in times:
            times[word]+=1
        else:
            times[word]=1
    ans=[]
    for i in xrange(min(lenword,lenstr-lensubstr+1)):
        self.findAnswer(i,lenstr,lenword,lensubstr,s,times,ans)
    return ans
def findAnswer(self,strstart,lenstr,lenword,lensubstr,s,times,ans):
    wordstart=strstart
    curr={}
    while strstart+lensubstr<=lenstr:
        word=s[wordstart:wordstart+lenword]
        wordstart+=lenword
        if word not in times:
            strstart=wordstart
            curr.clear()
        else:
            if word in curr:
                curr[word]+=1
            else:
                curr[word]=1
            while curr[word]>times[word]:
                curr[s[strstart:strstart+lenword]]-=1
                strstart+=lenword
            if wordstart-strstart==lensubstr:
                ans.append(strstart)
