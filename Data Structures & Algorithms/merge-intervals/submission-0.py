class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []

        for start, end in intervals:
            if not result:
                result.append([start, end])
            else: 
                last_end = result[-1][1]

                if start <= last_end:
                    result[-1][1] = max(last_end, end)
                else:
                    result.append([start, end])

        return result