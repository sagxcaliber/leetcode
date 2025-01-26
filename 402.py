def longestPalindrome( s: str) -> int:
    result = ""
    resIdx = 0
    for x in range(len(s)):
        r , l = x , x
        while l>=0 and r<len(s) and l-r+1< len(s) and s[l] == s[r]:
            if resIdx <  r+1-l:
                result = s[l:r+1]
                resIdx = len(result)
            r +=1
            l -=1
            
    return resIdx

print(longestPalindrome('arora'))