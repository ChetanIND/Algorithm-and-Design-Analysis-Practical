# Write a program to find the shortest path from a vertex to all other vertices of a weighted graph using Bellman Ford algorithm.
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices in the graph
        self.graph = []  # List to store the edges and their weights

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])  # Add an edge (u, v) with weight w to the graph

    def bellman_ford(self, src):
        dist = [
            float("inf")
        ] * self.V  # Initialize distances from the source to all vertices as infinity
        dist[src] = 0  # Distance from the source to itself is 0

        # Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Check for negative-weight cycles
        for u, v, w in self.graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains a negative-weight cycle")
                return

        # Print the distances from the source to all vertices
        print("Vertex \t Distance from Source")
        for i in range(self.V):
            print(f"{i}\t{dist[i]}")


if __name__ == "__main__":
    # Input from the user
    V = int(input("Enter the number of vertices: "))  # Number of vertices in the graph
    E = int(input("Enter the number of edges: "))  # Number of edges in the graph

    g = Graph(V)  # Create a graph with V vertices

    # Input edges and weights
    for _ in range(E):
        u, v, w = map(int, input("Enter edge (u v w): ").split())
        g.add_edge(u, v, w)

    src = int(
        input("Enter the source vertex: ")
    )  # Source vertex for finding shortest paths

    g.bellman_ford(src)  # Find and print the shortest paths
