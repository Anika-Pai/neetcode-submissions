class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 0
            
            seen[num] += 1
        
        freqs = sorted(seen.items(), key=lambda x: x[1], reverse=True)

        answer = []

        for item in freqs[:k]:
            answer.append(item[0])
        
        return answer

