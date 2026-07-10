from bisect import bisect_right

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """

       
        arr = sorted((nums[i], i) for i in range(n))
        vals = [x for x, _ in arr]

        
        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

       
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid


        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect_right(vals, vals[i] + maxDiff) - 1


        LOG = max(1, n.bit_length())
        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            pu, pv = pos[u], pos[v]
            if pu > pv:
                pu, pv = pv, pu

        
            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue

            cur = pu
            steps = 0

        
            for k in range(LOG - 1, -1, -1):
                nxt_pos = up[k][cur]
                if nxt_pos < pv:
                    cur = nxt_pos
                    steps += 1 << k

            ans.append(steps + 1)

        return ans