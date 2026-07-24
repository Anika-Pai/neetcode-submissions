class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_nums = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        top_k = sorted_nums[:k]
        
        result = []
        for num, count in top_k:
            result.append(num)
        
        return result