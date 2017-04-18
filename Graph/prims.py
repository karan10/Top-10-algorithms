# link - http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/
# April 18, 2017

class Prims:

    def __init__(self):
        self.__V = 5

    def __get_min(self, dist, visited):

        minimum = float("inf")

        for i in range(0,self.__V):
            if visited[i] is False and dist[i] < minimum: 
                minimum = dist[i]
                min_index = i

        return min_index


    def __print_solution(self, parent, dist, graph):
        
        print "Path     Distance";
        for v in range(0, self.__V):
            print "%d - %d    %d" % ( parent[v], v, graph[v][parent[v]] )


    def prim_mst(self, graph, source):

        dist, visited, parent = [float("inf")]*self.__V, [False]*self.__V, [False]*self.__V
        dist[0] = 0

        for c in range(0, self.__V-1):

            u = self.__get_min(dist, visited)

            visited[u] = True

            for v in range(0, self.__V):
                if visited[v] is False and graph[u][v] and dist[v] > graph[u][v]:
                    dist[v] = graph[u][v]
                    parent[v]  = u

        self.__print_solution(parent, dist, graph)


if __name__ == "__main__":

    graph =  [[0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0]]


            

    obj = Prims()
    obj.prim_mst(graph, 0)
