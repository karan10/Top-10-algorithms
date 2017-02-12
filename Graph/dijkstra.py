# link - http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
# February 12, 2017

class Dijkatra:

    def __init__(self):
        self.__V = 9

    def __get_min(self, dist, visited):

        minimum = float("inf")

        for i in range(0,self.__V):
            if visited[i] is False and dist[i] < minimum: 
                minimum = dist[i]
                min_index = i

        return min_index


    def __print_solution(self, dist):
        
        print "Vertex   Distance from Source";
        for v in range(0, self.__V):
            print "%d \t\t %d" % ( v, dist[v] )


    def smallest_path(self, graph, source):

        dist, visited = [float("inf")]*self.__V, [False]*self.__V,
        dist[0] = 0

        for c in range(0, self.__V-1):

            u = self.__get_min(dist, visited)

            visited[u] = True

            for v in range(0, self.__V):
                if visited[v] is False and graph[u][v] and dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]

        self.__print_solution(dist)


if __name__ == "__main__":

    graph =  [[0, 4, 0, 0, 0, 0, 0, 8, 0],
              [4, 0, 8, 0, 0, 0, 0, 11, 0],
              [0, 8, 0, 7, 0, 4, 0, 0, 2],
              [0, 0, 7, 0, 9, 14, 0, 0, 0],
              [0, 0, 0, 9, 0, 10, 0, 0, 0],
              [0, 0, 4, 14, 10, 0, 2, 0, 0],
              [0, 0, 0, 0, 0, 2, 0, 1, 6],
              [8, 11, 0, 0, 0, 0, 1, 0, 7],
              [0, 0, 2, 0, 0, 0, 6, 7, 0]];

    obj = Dijkatra()
    obj.smallest_path(graph, 0)
