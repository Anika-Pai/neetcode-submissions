class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, stone in enumerate(stones):
            stones[i] = -stone
        
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -(x - y))
            
        if stones:
            return -stones[0]
        
        return 0