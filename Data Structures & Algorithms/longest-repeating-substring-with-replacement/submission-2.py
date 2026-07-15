class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, length = 0,0 
        freqMap = {}
        for r in range(len(s)):
            if s[r] not in freqMap:
                freqMap[s[r]] = 1
            else:
                freqMap[s[r]] += 1
            
            windowLength = r - l + 1
            maxFreq = max(freqMap.values())
             
            while windowLength - maxFreq > k:
                freqMap[s[l]] -= 1
                l += 1
                windowLength = r - l + 1
                maxFreq = max(freqMap.values())

            length = max(length, windowLength)
        return length
            
        


                
                





        