class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        output = []
        for elem in nums:
            if elem in freq.keys():
                freq[elem] += 1
            else:
                freq[elem] = 0
        
        for i in range(k):
            highest_val = max(freq, key=freq.get)
            freq.pop(highest_val)
            output.append(highest_val)
        return output

        