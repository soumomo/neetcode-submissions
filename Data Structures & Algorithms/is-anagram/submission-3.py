class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMaps = {}
        countMapt = {}

        for char in s:
            if char not in countMaps:
                countMaps[char] = 1
            else:
                countMaps[char] += 1
        

        for char in t:
            if char not in countMapt:
                countMapt[char] = 1
            else:
                countMapt[char] += 1
        
        return (countMaps == countMapt)
                
        