class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        op = []
        for interval in intervals:
            if not op or op[-1][1] < interval[0]:
                op.append(interval)
            else:
                op[-1][1] = max(op[-1][1], interval[1])

        return op
