class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # i will create a dictionary where i will store key i.e the unique number and value i.e the frequency of it appearing
        frequencies = {}

        for element in nums:
            if element in frequencies:
                frequencies[element] += 1
            else:
                frequencies[element] = 1   

        return sorted(frequencies, key=frequencies.get, reverse=True)[:k]

             


            
        