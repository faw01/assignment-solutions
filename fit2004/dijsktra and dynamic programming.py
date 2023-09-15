import heapq
"""
Last modified: 28/04/2023
Version: Final
"""
class Edge():
    def __init__(self, u, v, w) -> None:
        """
        Function description:
            Constructor for Edge.

        :Input:
            u (Vertex): source vertex of the edge.
            v (Vertex): destination vertex of the edge.
            w (int): weight of the edge, which in this case is the time.

        :Attributes:
            u: source vertex of the edge.
            v: destination vertex of the edge.
            w: weight of the edge, which in this case is the time.

        :Time complexity:
            O(1)

        :Aux space complexity:
            O(1)
        """
        self.u = u
        self.v = v
        self.w = w

    def __str__(self) -> str:
        """
        Function description:
            A friendly string representation of the Edge.

        :Output:
            String in the format of "source --(weight)--> destination"

        :Time complexity:
            O(1)

        :Aux space complexity:
            O(1)
        """
        return f"{self.u} --({self.w})--> {self.v}"

class Vertex():
    def __init__(self, id) -> None:
        """
        Function description:
            Constructor for Vertex.

        :Input:
            id (int): unique id for a vertex.

        :Attributes:
            id (int): unique id for a vertex.
            edges (List[Edge]): A list of edges connected to the vertex.
            previous (Vertex): The previous vertex in the path, used in graph traversal algorithms.
            discovered (bool): A boolean flag indicating if the vertex has been discovered.
            visited (bool): A boolean flag indicating if the vertex has been visited.
            distance (int): The distance from the starting vertex in a graph traversal algorithm.

        :Time complexity:
            O(1)

        :Aux space complexity:
            O(1)
        """
        self.id = id
        self.edges = []
        self.previous = None
        self.discovered = False
        self.visited = False
        self.distance = 0

    def append_edge(self, edge) -> None:
        """
        Function description:
            Appends an edge to the vertex's edges list.

        :Input:
            edge (Edge): Edge object to be appended to the vertex's edges list.

        :Time complexity:
            O(1)

        :Aux space complexity:
            O(1)
        """
        self.edges.append(edge)
    
    def discover_vertex(self) -> None:
        """
        Function description:
            Marks the vertex as discovered.

        :Output:
            None

        :Time complexity:
            O(1)

        :Aux space complexity:
            O(1)
        """
        self.discovered = True
    
    def visit_vertex(self) -> None:
        """
        Function description:
            Marks the vertex as visited.

        :Output:
            None

        :Time complexity:
            O(1)

        :Aux space complexity:
            O(1)
        """
        self.visited = True

    def reset_vertex(self) -> None:
        """
        Function description:
            Resets the vertex's discovered, visited, and previous properties.

        :Output:
            None

        :Time complexity:
            O(1)

        :Aux space complexity:
            O(1)
        """
        self.discovered = False
        self.visited = False
        self.previous = None
    
    def __str__(self) -> str:
        """
        Function description:
            Returns a string representation of the vertex, including its id and edges.

        :Output:
            str: String representation of the vertex.

        :Time complexity:
            O(n) where n is the length of self.edges

        :Aux space complexity:
            O(1)
        """
        edges_str = "\n with edges: ".join(str(edge) for edge in self.edges)
        return f'{self.id}\n with edges: {edges_str}' if edges_str else f'{self.id}'

class Graph():
    def __init__(self, num_vertices) -> None:
        """
        Function description:
            Constructor for Graph.
            
            This uses an adjacency list representation.

        :Input:
            num_vertices (int): The number of vertices in the graph.

        :Attributes:
            vertices: A list of vertices in the graph.

        :Time complexity:
            O(n) where n is the number of vertices

        :Aux space complexity:
            O(n) where n is the number of vertices
        """
        self.vertices = [None] * num_vertices

        for i in range(num_vertices):
            self.vertices[i] = Vertex(i)

    def reset(self) -> None:
        """
        Function description:
            Resets the vertices to its original state.

        :Time complexity:
            O(n) where n is the number of vertices in self.vertices.

        :Aux space complexity:
            O(1)
        """
        for vertex in self.vertices:
            vertex.reset_vertex()

    def add_edge(self, u, v, w, directed = True) -> None:
        """
        Function description:
            Adds an edge.

        :Input:
            u (Vertex): source vertex of the edge.
            v (Vertex): destination vertex of the edge.
            w (int): weight of the edge, which in this case is the time.
            directed (bool): indicates if the edge is directed or undirected,
                             if undirected, adds edges to and from vertexes.
        
        :Time complexity:
            O(1)

        :Aux space complexity:
            O(1)
        """
        current_edge = Edge(u, v, w)
        current_vertex = self.vertices[u]
        current_vertex.append_edge(current_edge)

        if directed == False:
            current_edge = Edge(v, u, w)
            current_vertex = self.vertices[v]
            current_vertex.append_edge(current_edge)

    def build_path(self, vertex) -> list:
        """
        Function description:
            Builds the path from the starting vertex to the given vertex.

        :Input:
            vertex (Vertex): The destination vertex.

        :Output:
            A list containing the path from the starting vertex to the given vertex.

        :Time complexity:
            O(n) where n is the number of vertices in the path.

        :Aux space complexity:
            O(n) where n is the number of vertices in the path.
        """
        path = []
        while vertex is not None:
            path.append(vertex)
            vertex = self.vertices[vertex].previous

        reversed_path = []
        for i in range(len(path) - 1, -1, -1):
            reversed_path.append(path[i])

        return reversed_path

    def dijkstra(self, source, destination):
        """
        Function description:
            Dijkstra's algorithm to find the shortest path between the source and destination vertices.

        :Input:
            source (int): The starting vertex.
            destination (int): The ending vertex.

        :Output:
            A tuple containing the shortest path distance and the path as a list of vertex indices.

        :Time complexity:
            O((|V| + |E|) * log|V|) where |V| is the number of vertices and |E| is the number of edges in the graph.

        :Aux space complexity:
            O(|V|) where |V| is the number of vertices in the graph.
        """
        # reset the vertices to their initial state
        self.reset()

        # initialize the distance list and set the distance of the source vertex to 0
        vertex_distances = [float('inf')] * len(self.vertices)
        vertex_distances[source] = 0

        # create a priority queue and add the source vertex with distance 0
        priority_queue = [(0, source)]
        self.vertices[source].discover_vertex()

        # process vertices in the priority queue until it's empty
        while priority_queue:
            # get the vertex with the smallest distance from the priority queue
            current_distance, current_vertex_id = heapq.heappop(priority_queue)

            # skip the vertex if it has been visited already
            if self.vertices[current_vertex_id].visited:
                continue

            # mark the current vertex as visited and update its distance
            self.vertices[current_vertex_id].visit_vertex()
            vertex_distances[current_vertex_id] = current_distance

            # iterate over the edges of the current vertex
            for edge in self.vertices[current_vertex_id].edges:
                # get the neighbor vertex id
                neighbor_vertex_id = edge.v
                if neighbor_vertex_id == current_vertex_id:
                    neighbor_vertex_id = edge.u 

                # calculate the distance to the neighbor vertex
                new_neighbor_distance = current_distance + edge.w
                neighbor_vertex = self.vertices[neighbor_vertex_id]

                # skip the neighbor vertex if it has been visited already
                if neighbor_vertex.visited:
                    continue

                # update the neighbor vertex's distance and previous vertex if the new distance is smaller
                if new_neighbor_distance < vertex_distances[neighbor_vertex_id]:
                    vertex_distances[neighbor_vertex_id] = new_neighbor_distance
                    neighbor_vertex.previous = current_vertex_id

                    # add the neighbor vertex with the updated distance to the priority queue
                    heapq.heappush(priority_queue, (new_neighbor_distance, neighbor_vertex_id))

        # return the shortest distance and the path to the destination vertex
        return vertex_distances[destination], self.build_path(destination)
    
    def __str__(self) -> str:
        """
        Function description:
            Returns a string representation of the graph.
        
        :Output:
            A string representing the graph in the format "vertex1, vertex2, ...".

        :Time complexity:
            O(n) where n is the number of vertices in the graph.

        :Aux space complexity:
            O(n) where n is the number of vertices in the graph.
        """
        return "\n".join(str(vertex) for vertex in self.vertices)
    
def optimalRoute(start, end, passengers, roads):
    """
    Written by: faw

    Precondition:
        start and end are integers representing the start and end vertices, passengers is a list of integers representing the passenger vertices, roads is a list of tuples (a, b, c, d) where a and b are integer vertices, c is the weight of the solo lane, and d is the weight of the carpool lane.

    Postcondition: 
        returns a list of vertices representing the shortest path between the start and end points.

    Function description: 
        Returns the optimal route to go from the start to end with the least total travel time

    Approach description: 
        By constructing a layered graph, and offseting the vertices, Dijsktra's algorithm can be run on a large graph to determine which is the most optimal route to take. Edges are added to the graph for both solo and carpool lanes, and zero-weight edges are added between non-carpool and carpool vertices for each passenger. 

    Input:
        start: integer representing the start vertex.
        end: integer representing the end vertex.
        passengers: list of integers representing the passenger vertices.
        roads: list of tuples (a, b, c, d) where a and b are integer vertices, c is the weight of the solo lane, and d is the weight of the carpool lane.

    Output:
        A list of vertices representing the shortest path between the start and end points.

    Time complexity:
        where r is the number of roads in the graph and l is the number of locations

        Best Case: O((r log l)) * could be cases that start == end so it would be O(1)
        Worst Case: O((r log l)) 

    Space complexity:
        Auxiliary: O(l + r) 
    """
    # finds the maximum vertex among the roads to be used as the number of vertices in the graph, it does so just by iteration, then the maximum location number is incremented by 1 to account for the total number of locations, since location ids are zero based
    max_location = 0
    for a, b, _, _ in roads:
        max_location = max(max_location, a, b)
    num_locations = max_location + 1

    # since we are connected two graphs to produce two layers, we multiply it by 2 so the graph is intialised double the number of locations, representing both solo and carpool
    layer = num_locations * 2
    graph = Graph(layer)

    # adds the edges for both non-carpool and carpool lanes to the graph by iterating through the roads list, creating an edge for each road, there is also an offset of the carpool layers that occurs so the vertices in solo can be linked to the vertices in carpool, finally if there are passengers, it also adds edges with zero weight to connect the non-carpool and carpool vertices for each passenger.
    for a, b, c, d in roads:
        graph.add_edge(a, b, c)
        graph.add_edge(a + num_locations, b + num_locations, d)
        if passengers:
            for passenger in passengers:
                graph.add_edge(passenger, passenger + num_locations, 0)

    # computes the shortest path between the start and end vertices for both non-carpool and carpool layers, using dijkstra's algorithm
    solo_path_weight, solo_path = graph.dijkstra(start, end)
    carpool_path_weight, carpool_path = graph.dijkstra(start, end + num_locations)

    # compares the weights of the solo and carpool paths and selects the one with the smaller weight, for example, if the solo path is shorter, the unique_path is set to solo_path or if the carpool path is shorter, the carpool path's vertices are converted back to their original location indices (by taking the modulo with num_locations), and the duplicates are removed
    if solo_path_weight < carpool_path_weight:
        unique_path = solo_path
    else:
        for i in range(len(carpool_path)):
            carpool_path[i] %= num_locations

        unique_path = []
        for i in range(len(carpool_path)):
            if i == 0 or carpool_path[i] != carpool_path[i - 1]:
                unique_path.append(carpool_path[i])

    return unique_path

def select_sections(occupancy_probability):
    """
    Written by: faw

    Precondition: 
        occupancy_probability is a non-empty matrix of positive integers, dimensions are n * m and n > m
        remove only one section from each of the n rows
        minimise the amount of shuffling work required, hence, 

    Postcondition:
        list of indices of n sections that has the total minimum occupancy rate for the entire matrix

    Function description:  
        Calculates the minimum total occupancy probability and the section locations for each row with the minimum occupancy probability by using dynamic programming.

    Approach description: 
        Using dynamic programming, a memo can be used to store the minimum total occupancy probabilities for each cell in the occupancy_probability matrix. Then, the memo is constructed in a row-by-row manner, and for each cell, the function checks the adjacent cells in the previous row to find the minimum total occupancy probability. After memo is finished processing, the function backtracks from the last row, finding the optimal section locations for each row that lead to the minimum total occupancy probability, generating a path to it.

    Input:
        occupancy_probability: matrix representing the occupancy probability

    Output: 
        Returns a list containing the minimum total occupancy probability and the list of section locations for each row.

        minimum_total_occupancy - total occupancy for selected sections

        sections_location - list of tuples representing the selected sections in row, column format

    Time complexity: 
        where n is the number of rows and m is the number of columns

        Best Case: O(n * m)
        Worst Case: O(n * m)

    Space complexity:
        Auxilary: O(n * m)
    """
    # n is the number of rows whilst m is the number of columns or aisles
    n = len(occupancy_probability)
    m = len(occupancy_probability[0])

    # initialization of the memo, creates a nested list with the same dimensions as occupancy_probability and fills it with inf values
    memo = [[float('inf') for i in range(m)] for j in range(n)] 

    # fill the first row of the memo with the initial row of the occupancy_probability
    for i in range(m):
        memo[0][i] = occupancy_probability[0][i]

    # iterate through the rows of occupancy_probability, starting from the second row as the first row is already processsed, then iterate through the columns of the occupancy_probability, and lastly iterate through the adjacent columns in the previous row e.g. k = j-1, j, j+1, from here check if k is within the valid column range, and if it is calculate the current total occupancy probability by adding the value of the current cell and the adjacent cell in the previous row whilst checking if the current total occupancy probability is less than the stored value in the memo list and if it is, updating the memo list with the new minimum total occupancy probability
    for i in range(1, n): 
        for j in range(m): 
            for k in range(j - 1, j + 2): 
                if k >= 0 and k < m: 
                    current_occupancy = occupancy_probability[i][j] + memo[i - 1][k]    
                    if memo[i][j] > current_occupancy:
                        memo[i][j] = current_occupancy 

    # gets the minimum total occupancy in the last row of memo by iterating over it and updating
    minimum_total_occupancy = memo[-1][0]  
    for value in memo[-1]:  
        if value < minimum_total_occupancy:
            minimum_total_occupancy = value  

    sections_location = []
    
    # iterates through the last row of the memo table and finds the index of minimum_total_occupancy
    minimum_total_occupancy_index = 0
    for i in range(1, m):
        if memo[-1][i] < memo[-1][minimum_total_occupancy_index]:
            minimum_total_occupancy_index = i

    # backtracking begins here by iterating through the rows in reverse order, starting from the second last row as the last row has been processed already, moving up to the first row, for each row, it checks the adjacent cells (j) in the previous row that led to the minimum total occupancy probability, where j is in {minimum_total_occupancy_index-1, minimum_total_occupancy_index, minimum_total_occupancy_index+1} and lastly it appends the current cell (i, minimum_total_occupancy_index) to the sections_location list and updates the minimum_total_occupancy_index to the column of the previous row's cell that led to the minimum total occupancy probability.
    for i in range(n - 1, 0, -1):
        for j in range(minimum_total_occupancy_index - 1, minimum_total_occupancy_index + 2):
            if j >= 0 and j < m:
                if memo[i][minimum_total_occupancy_index] == occupancy_probability[i][minimum_total_occupancy_index] + memo[i - 1][j]:
                    sections_location.append((i, minimum_total_occupancy_index))
                    minimum_total_occupancy_index = j
                    break

    # finally add back the first row    
    sections_location.append((0, minimum_total_occupancy_index))

    # reverse the order by iterating through the first half of the list, swapping each element with its corresponding element at the opposite end of the list e.g. first goes to last, second goes to second last, etc
    for i in range(len(sections_location) // 2):
        sections_location[i], sections_location[len(sections_location) - i - 1] = sections_location[len(sections_location) - i - 1], sections_location[i]
        
    return [minimum_total_occupancy, sections_location]

if __name__ == "__main__":
    # Example 1 - Q1
    start = 0
    end = 4
    passengers = [2, 1]
    roads = [(0, 3, 5, 3), (3, 4, 35, 15), (3, 2, 2, 2), (4, 0, 15, 10),
    (2, 4, 30, 25), (2, 0, 2, 2), (0, 1, 10, 10), (1, 4, 30, 20)]
    res = optimalRoute(start, end, passengers, roads)
    print(res)

    # Example 2 - Q2
    occupancy_probability = [
    [31, 54, 94, 34, 12],
    [26, 25, 24, 16, 87],
    [39, 74, 50, 13, 82],
    [42, 20, 81, 21, 52],
    [30, 43, 19, 5, 47],
    [37, 59, 70, 28, 15],
    [ 2, 16, 14, 57, 49],
    [22, 38, 9, 19, 99]]
    res = select_sections(occupancy_probability)
    print(res)