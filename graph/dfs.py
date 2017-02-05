from collections import defaultdict


class DFS:

    def __init__(self):
        self.graph = defaultdict(list)

    def create_edge(self, u, v):
        self.graph[u].append(v)


    def __dfs_traverse(self, n, visited):
        visited[n] = True
        print n
        for i in self.graph[n]:
            if not visited[i]:
                self.__dfs_traverse(i, visited)

    def dfs_call(self, start):
        visited = [False] * len(self.graph)
        self.__dfs_traverse(start, visited)
        


if __name__ == "__main__":

    obj = DFS()
    obj.create_edge(0, 1)
    obj.create_edge(0, 2)
    obj.create_edge(1, 2)
    obj.create_edge(2, 0)
    obj.create_edge(2, 3)
    obj.create_edge(3, 3)
    obj.dfs_call(2)
