class Solution:
    def findJudge(self, N, trust):
        if N == 1:
            return 1
        
        di = {i:[] for i in range(1, N+1)}

        for pair in trust:
            di[pair[0]].append(pair[1])

        empty_val = 0
        idx = 0
        for k in di:
            if di[k] == []:
                empty_val += 1
                idx = k

        if not empty_val == 1:
            return -1

        list_sets = [set(v) for k, v in di.items() if k != idx]

        intersec = list_sets[0].intersection(*list_sets[1:])

        if len(intersec) == 1:
            return list(intersec)[0]
        return -1