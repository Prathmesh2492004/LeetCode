class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete = 0

        def dfs(node):
            visited[node] = True
            vertices.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                vertices = []
                dfs(i)

                k = len(vertices)

                edge_count = 0
                for v in vertices:
                    edge_count += len(graph[v])

                edge_count //= 2

                if edge_count == k * (k - 1) // 2:
                    complete += 1

        return complete
        