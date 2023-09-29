class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices in the graph
        self.graph = [
            [0 for _ in range(vertices)] for _ in range(vertices)
        ]  # Initialize an empty adjacency matrix

    def is_safe(self, v, pos, c, color):
        # Check if it's safe to color vertex v with color c
        for i in range(self.vertices):
            if self.graph[v][i] == 1 and color[i] == c:
                return False  # If an adjacent vertex has the same color, it's not safe
        return True

    def graph_coloring_util(self, m, color, v):
        if v == self.vertices:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, 0, c, color):  # Pass '0' as the second argument
                color[v] = c
                if self.graph_coloring_util(m, color, v + 1):
                    return True
                color[v] = 0

    def graph_coloring(self, m):
        color = [0] * self.vertices  # Initialize an array to store vertex colors
        if not self.graph_coloring_util(m, color, 0):
            return False  # If no valid coloring exists, return False

        print("Solution exists: Following are the assigned colors:")
        for c in color:
            print(c, end=" ")  # Print the colors assigned to each vertex
        return True


# Example usage:
if __name__ == "__main__":
    g = Graph(4)
    g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    m = 3  # Number of colors
    if g.graph_coloring(m):
        print("\nGraph is colorable")
    else:
        print("\nGraph is not colorable")
