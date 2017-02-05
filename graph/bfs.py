from collections import defaultdict


class BFS:

    def __init__(self):
        self.graph = defaultdict(list)

    def create_edge(self, u, v):
        self.graph[u].append(v)


    def bfs_traverse(self, start):
        visited, queue = [False]*len(self.graph), []
        queue.append(start)
        visited[start] = True
        while queue:
            s = queue.pop(0)
            print s
            for n in self.graph[s]:
                if not visited[n]:
                    visited[n] = True
                    queue.append(n)


if __name__ == "__main__":

    obj = BFS()
    obj.create_edge(0, 1)
    obj.create_edge(0, 2)
    obj.create_edge(1, 2)
    obj.create_edge(2, 0)
    obj.create_edge(2, 3)
    obj.create_edge(3, 3)
    obj.bfs_traverse(2)

    # print bfs_obj
