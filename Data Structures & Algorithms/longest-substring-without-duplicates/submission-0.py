class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()        
        l,r = 0, 0
        maximum = 0
        while r < len(s):
            char = s[r] 
            if char in window:
                window.remove(s[l])
                l += 1
            else:
                window.add(char)
                r += 1
                maximum = max(len(window), maximum)
        return maximum



             

        