from queue import PriorityQueue;
class Graph:
    def __init__(self,vertices):
        self.v=vertices;
        self.edges=[[-1 for i in range(vertices)] for j in range(vertices)];
        self.visit=[];

    def AddEgde(self,u,v,wt):
        self.edges[u][v] = wt;
        self.edges[v][u] = wt;
def dijkstra(graph,src):
    D = {v:float('inf') for v in range(graph.v)};
    D[src] = 0;

    pq=PriorityQueue();
    pq.put((0,src));

    while not pq.empty():
        (dist,cr_vertex)=pq.get();
        graph.visit.append(cr_vertex);

        for nbr in range(graph.v):
            if graph.edges[cr_vertex][nbr]!=-1:
                distance=graph.edges[cr_vertex][nbr];
                if nbr not in graph.visit:
                    old_cost=D[nbr];
                    new_cost=D[cr_vertex]+distance;
                    if new_cost < old_cost:
                        pq.put((new_cost,nbr));
                        D[nbr] = new_cost;
    return D;
if __name__=="__main__":
    g=Graph(9);
    g.AddEgde(0, 1, 4);
    g.AddEgde(0, 6, 7);
    g.AddEgde(1, 6, 11);
    g.AddEgde(1, 7, 20);
    g.AddEgde(1, 2, 9);
    g.AddEgde(2, 3, 6);
    g.AddEgde(2, 4, 2);
    g.AddEgde(3, 4, 10);
    g.AddEgde(3, 5, 5);
    g.AddEgde(4, 5, 15);
    g.AddEgde(4, 7, 1);
    g.AddEgde(4, 8, 5);
    g.AddEgde(5, 8, 12);
    g.AddEgde(6, 7, 1);
    g.AddEgde(7, 8, 3);

    D=dijkstra(g,0);

    print(D);

    for vertex in range(len(D)):
        print("Distance from vertex 0 to vertex", vertex, "is", D[vertex]);
