from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])

        start_health = health - grid[0][0]

        if start_health <= 0:
            return False

        best = [[-1] * n for _ in range(m)]
        best[0][0] = start_health

        q = deque([(0, 0, start_health)])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, h = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    nh = h - grid[nr][nc]

                    if nh > 0 and nh > best[nr][nc]:
                        best[nr][nc] = nh
                        q.append((nr, nc, nh))

        return False