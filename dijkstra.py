from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, v1, v2, weight):
        self.edges[v1].append((v2, weight))
        self.edges[v2].append((v1, weight))


    def dijkstra(self, start, end):

        unvisited = []
        prev  = {}
        dist = {}

        for k in self.edges.keys():
            dist[k] = float('Inf')
            prev[k] = None
            unvisited.append(k)

        dist[start] = 0

        while unvisited:

            current = None
            min_d = float('Inf')

            for (v, d) in dist.items():
                if v in unvisited and d < min_d:
                    min_d = d
                    current = v

            unvisited.remove(current)

            neighbors = self.edges[current]
            for (v, w) in neighbors:
                new_dist = dist[current] + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    prev[v] = current

        path = []
        current = end

        while start not in path:
            path = [current] + path
            current = prev[current]

        length = dist[end]
        return (path, length)


g = Graph()
g.add_edge(1, 2, 7)
g.add_edge(1, 3, 9)
g.add_edge(1, 6, 14)
g.add_edge(2, 3, 10)
g.add_edge(2, 4, 15)
g.add_edge(3, 4, 11)
g.add_edge(3, 6, 2)
g.add_edge(4, 5, 6)
g.add_edge(5, 6, 9)

path, weight = g.dijkstra(1, 5)
print(path, weight)
