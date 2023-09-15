"""
Last modified: 26/5/2023
Version: Final
"""
from collections import deque

# ==================== Q1 ====================
class NetworkVertex:
    """
    NOTE: Taken from my Assignment 1

    Class representing a vertex in the network.

    Precondition:
        None

    Postcondition:
        A NetworkVertex object is created with discovered, visited and previous set to default values.

    Input:
        id: Integer representing the id of the vertex.

    Time complexity:
        Best:
            O(1)
        Worst: 
            O(1)

    Space complexity:
        Input: 
            O(1)
        Aux: 
            O(1)
    """
    def __init__(self, id):
        self.id = id    
        self.edges = [] 
        self.discovered = False
        self.visited = False
        self.previous = None
        
    def discover_vertex(self):
        """
        Function description:
            Marks the vertex as discovered.

        Precondition:
            None

        Postcondition:
            The vertex's discovered property is set to True.

        Input:
            None

        Return:
            None

        Time complexity:
            Best:
                O(1)

            Worst:
                O(1)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)
        """
        self.discovered = True

    def visit_vertex(self):
        """
        Function description:
            Marks the vertex as visited.
        
        Precondition:
            None

        Postcondition:
            The vertex's visited property is set to True.

        Input:
            None

        Return:
            None

        Time complexity:
            Best:
                O(1)

            Worst:
                O(1)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)
        """
        self.visited = True

    def reset_vertex(self):
        """
        Function description:
            Resets the vertex to its original state.

        Precondition:
            None

        Postcondition:
            The vertex's discovered, visited and previous properties are set to their default values.

        Input:
            None

        Return:
            None

        Time complexity:
            Best:
                O(1)

            Worst:
                O(1)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)
        """
        self.discovered = False
        self.visited = False
        self.previous = None

    def add_edge(self, edge):
        """
        Function description:
            Adds an edge to the vertex's edge list.

        Precondition:
            None
        
        Postcondition:
            The edge is added to the vertex's edge list.

        Input:
            edge (NetworkEdge): Edge to be added to the vertex's edge list.

        Return:
            None

        Time complexity:
            Best:
                O(1)

            Worst:
                O(1)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)
        """
        self.edges.append(edge)

class NetworkEdge:
    """
    Class representing an edge in the network.

    NOTE: Taken from my Assignment 1

    Input
        u (int): Source vertex id.
        v (int): Destination vertex id.
        flow (int): Flow of the edge.
        capacity (int): Capacity of the edge.
    
    Postcondition
        The object is instantiated with the given attributes and the residual is calculated as capacity - flow, other attributes include the reverse edge and the residual.

    Time complexity
        Best:
            O(1)

        Worst:
            O(1)
    
    Space complexity:
        Input:
            O(1)

        Aux:
            O(1)
    """
    def __init__(self, u, v, flow, capacity) -> None:
        self.u = u
        self.v = v
        self.flow = flow
        self.capacity = capacity
        self.residual = self.capacity - self.flow
        self.reverse = None

    def add_flow(self, flow_amount):
        """
        Function description:
            Adds flow to the edge and updates the residual. If the edge is a reverse edge, the residual of the reverse edge is also updated.

        Input:
            flow_amount (int): Amount of flow to be added to the edge.
        
        Output:
            None

        Time complexity:
            Best:
                O(1)

            Worst:
                O(1)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)
        """
        self.flow += flow_amount
        self.residual -= flow_amount

        if self.reverse:
            self.reverse.residual += flow_amount

class ResidualNetwork:
    """
    Class representing a residual network with vertices and the super source and sink.

    Input:
        vertices (int): Number of vertices in the network.

    Precondition:
        None
        
    Postcondition:
        A ResidualNetwork object is created with the given number of vertices.

    Time complexity:
        Best:
            O(1)

        Worst:
            O(1)

    Space complexity:
        Input:
            O(1)

        Aux:
            O(1)
    """
    def __init__(self, vertices):
        self.vertices = deque([None] * (vertices))
        
        self.super_source = None
        self.super_sink = None

        for i in range(vertices):
            self.vertices[i] = NetworkVertex(i)

    def reset(self):
        """
        Function description:
            Resets the vertices to its original state.

        Precondition:
            None

        Postcondition:
            The vertices are reset to their original state.

        Input:
            None

        Output:
            None

        Time complexity:
            Best:
                O(V)

            Worst:
                O(V)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)
        """  
        for vertex in self.vertices:
            vertex.reset_vertex()

    def create_network(self, connections, is_residual=False):
        """
        Function description:
            Creates the network based on the connections.

        Precondition:
            All vertices have already been split.

        Postcondition:
            The network is created based on the connections.

        Input:
            connections (list): List of tuples representing the connections between vertices.
            is_residual (bool): Boolean representing whether the network is a residual network or not.

        Output:
            None

        Time complexity:
            Best:
                O(E)

            Worst:
                O(E)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)
        """
        for u, v, capacity in connections:
            u_out = u * 3 + 2  # compute the 'out' vertex of u
            v_in = v * 3  # compute the 'in' vertex of v
            if v == (len(connections) - 1):  # check if the edge is directed to the supersink
                self.add_edge(u_out, v_in, 0, float('inf'), is_residual)
            else:
                self.add_edge(u_out, v_in, 0, capacity, is_residual)  # use capacity as the capacity for other edges
            
    def add_edge(self, u, v, flow, capacity, is_residual=False):
        """
        Function description:
            Adds an edge to the network.

        Precondition:
            None

        Postcondition:
            The edge is added to the network.

        Input:
            u (int): Source vertex id.
            v (int): Destination vertex id.
            flow (int): Flow of the edge.
            capacity (int): Capacity of the edge.
            is_residual (bool): Boolean representing whether the edge is a residual edge or not.

        Output:
            None

        Time complexity:
            Best:
                O(1)

            Worst:
                O(1)

        Space complexity:
            Input:
                O(1)
            
            Aux:
                O(1)
        """
        forward_edge = NetworkEdge(u, v, flow, capacity)
        self.vertices[u].add_edge(forward_edge)
        backward_edge = NetworkEdge(v, u, capacity if is_residual else 0, capacity)
        self.vertices[v].add_edge(backward_edge)
        forward_edge.reverse = backward_edge
        backward_edge.reverse = forward_edge

    def create_super_sink(self, sinks):
        """
        Function description:
            Adds a super sink to the network and connects the 'out' vertices of the target vertices to the super sink.

        Precondition:
            Network has already been created.

        Postcondition:
            A super sink is added to the network and the 'out' vertices of the target vertices are connected to the super sink.


        Input:
            sinks (list): List of integers representing the target vertices.

        Output:
            None
            
        Time complexity:
            Best:
                O(1)

            Worst:
                O(1)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)
        """
        super_sink = len(self.vertices)
        self.vertices.append(NetworkVertex(super_sink))
        for sink in sinks:
            sink_out = sink * 3 + 2  # compute the 'out' vertex of the sink
            self.add_edge(sink_out, super_sink, 0, float('inf'))  # connect the 'out' vertex to the super sink
        self.super_sink = super_sink

    def create_super_source(self, origin, maxOut):
        """
        Function description:
            Adds a super source to the network and connects the 'in' vertices of the origin vertex to the super source.

        Precondition:
            Network has already been created.

        Postcondition:
            A super source is added to the network and the 'in' vertices of the origin vertex are connected to the super source.

        Input:
            origin (int): Integer representing the origin vertex.
            maxOut (list): List of integers representing the maximum out capacity of each vertex.

        Output:
            None

        Time complexity:
            Best:
                O(1)

            Worst:
                O(1)
                
        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)                
        """
        super_source = len(self.vertices)
        self.vertices.append(NetworkVertex(super_source))
        origin_v = origin * 3 + 1  # get the 'in' vertex of the origin
        self.add_edge(super_source, origin_v, 0, maxOut[origin])  # connect the super source to the origin
        self.super_source = super_source

    def build_path(self, sink):
        """
        Function description:
            Builds a path from the super sink to the super source.

        Precondition:
            None

        Postcondition:
            A path is built from the super sink to the super source.

        Input:
            sink (int): Integer representing the id of the sink.

        Output:
            path (list): List of NetworkVertex objects representing the path from the super sink to the super source.

        Time complexity:
            Best:
                O(V)

            Worst:
                O(V)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)
        """
        path = []

        u = self.vertices[sink]

        # backtrack
        while u.previous is not None:
            
            path.append(u)
            u = self.vertices[u.previous.u]

        return [path[i] for i in range(len(path) - 1, -1, -1)]

    def split_vertex(self, maxIn, maxOut):
        """
        Function description:
            Splits each vertex into 'in', 'original', and 'out' vertices.

        Precondition:
            None

        Postcondition:
            Each vertex is split into 'in', 'original', and 'out' vertices.

        Input:
            maxIn (list): List of integers representing the maximum in capacity of each vertex.
            maxOut (list): List of integers representing the maximum out capacity of each vertex.


        Output:
            None

        Time complexity:
            Best:
                O(V)

            Worst:
                O(V)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)
        """
        new_vertices = [None] * (3 * len(self.vertices))

        # for each vertex in the original network
        for i in range(len(self.vertices)):
            # create three new vertices
            vertex_in = NetworkVertex(i * 3)
            vertex_original = NetworkVertex(i * 3 + 1)
            vertex_out = NetworkVertex(i * 3 + 2)

            # add the new vertices to the new_vertices list
            new_vertices[vertex_in.id] = vertex_in
            new_vertices[vertex_original.id] = vertex_original
            new_vertices[vertex_out.id] = vertex_out

            # create an edge from the 'in' vertex to the original vertex with capacity equal to maxIn
            edge_in = NetworkEdge(vertex_in.id, vertex_original.id, 0, maxIn[i])
            vertex_in.add_edge(edge_in)

            # add backward edge
            backward_edge_in = NetworkEdge(vertex_original.id, vertex_in.id, 0, maxIn[i])
            vertex_original.add_edge(backward_edge_in)
            edge_in.reverse = backward_edge_in
            backward_edge_in.reverse = edge_in

            # create an edge from the original vertex to the 'out' vertex with capacity equal to maxOut
            edge_out = NetworkEdge(vertex_original.id, vertex_out.id, 0, maxOut[i])
            vertex_original.add_edge(edge_out)

            # add backward edge
            backward_edge_out = NetworkEdge(vertex_out.id, vertex_original.id, 0, maxOut[i])
            vertex_out.add_edge(backward_edge_out)
            edge_out.reverse = backward_edge_out
            backward_edge_out.reverse = edge_out

            # for each edge in the original vertex's edge list
            for edge in self.vertices[i].edges:
                # if the edge's destination is the original vertex, update it to the 'in' vertex
                if edge.v == i:
                    edge.v = vertex_in.id
                    vertex_in.add_edge(edge)

                # if the edge's source is the original vertex, update it to the 'out' vertex
                if edge.u == i:
                    edge.u = vertex_out.id
                    vertex_out.add_edge(edge)

        # replace the original vertices with the new vertices
        self.vertices = new_vertices

    def bfs(self, source, sink):
        """
        Function description:
            Performs a breadth-first search on the network.

        Precondition:
            None

        Postcondition:
            A breadth-first search is performed on the network.

        Input:
            source (NetworkVertex): Source vertex.
            sink (NetworkVertex): Sink vertex.

        Output:
            True if a path is found from the source to the sink, False otherwise.

        Time complexity:
            Best:
                O(V + E)

            Worst:
                O(V + E)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(V)
        """
        self.reset()
        
        queue = deque([source])

        source.discover_vertex()

        while queue:

            u = queue.popleft()
            
            if u == sink:
                return True
                        
            for edge in u.edges:
                v = self.vertices[edge.v]
                
                if not v.discovered and edge.residual > 0:

                    if v.previous is None: 
                        v.previous = edge

                    v.discover_vertex()
                    
                    queue.append(v)

        return False
    
    def ford_fulkerson(self, source, sink):
        """
        Function description:
            Performs the Ford-Fulkerson algorithm on the network.

        Precondition:
            Network has already been created with the super source and sink added.
        
        Postcondition:
            The Ford-Fulkerson algorithm is performed on the network.

        Input:
            source (NetworkVertex): Source vertex.
            sink (NetworkVertex): Sink vertex.

        Output:
            The maximum flow of the network.

        Time complexity:
            Best:
                O(V * E^2) where V is the number of vertices

            Worst:
                O(V * E^2)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)
        """
        max_flow = 0
        
        # while there is a path
        while self.bfs(self.vertices[source], self.vertices[sink]):

            # augment the path
            max_flow += self.augment_path(self.vertices[sink])

        return max_flow

    def augment_path(self, sink):
        """
        Function description:
            Augments the path from the super sink to the super source.

        Precondition:
            Residual Network has already been correctly set up.

        Postcondition:
            The path from the super sink to the super source is augmented.

        Input:
            sink (NetworkVertex): Sink vertex.

        Output:
            The minimum residual of the path.

        Time complexity:
            Best:
                O(V) where V is the number of vertices
            
            Worst:
                O(V)

        Space complexity:
            Input:
                O(1)

            Aux:
                O(1)
        """
        # build the path
        path = self.build_path(sink.id)
        min_residual = float('inf')

        # find the minimum residual
        for i in range(1, len(path) - 2):   
            edge = path[i].previous
            
            if edge.residual < min_residual:
                min_residual = edge.residual

        # augment the flow along the path
        for i in range(1, len(path) - 2):   
            edge = path[i].previous
            edge.add_flow(min_residual)
    
        return min_residual


def maxThroughput(connections, maxIn, maxOut, origin, targets):
    """
    Function description:
        Computes the maximum throughput of the network.

    Approach description:
        The maxThroughput function implements the Ford-Fulkerson algorithm to find the maximum flow or throughput in a network. It constructs a residual network by splitting each vertex into 'in', 'original', and 'out' vertices. The original network is represented using NetworkVertex and NetworkEdge classes, and the residual network is represented using the ResidualNetwork class.

        The function first initializes a residual network with the specified number of vertices. It then splits each vertex into 'in', 'original', and 'out' vertices, creating appropriate edges and capacities. Next, it creates the network by adding edges between the vertices based on the provided connections. If the network is residual, the capacities of the edges are set to infinity; otherwise, the capacities are set to the specified values.

        After creating the network, the function adds a super sink and connects the 'out' vertices of the target vertices to the super sink. It also adds a super source and connects the 'in' vertices of the origin vertex to the super source.

        The Ford-Fulkerson algorithm is then applied to find the maximum flow from the super source to the super sink. It iteratively performs a breadth-first search (BFS) on the residual network to find an augmenting path from the super source to the super sink. If such a path exists, the algorithm augments the flow along the path and updates the residual capacities of the edges. This process continues until no augmenting paths can be found.

        Finally, it returns the maximum flow as the maximum throughput from the origin to the targets in the network.

    Precondition:
        Resdiual Network set up correctly

    Postcondition:
        The maximum throughput of the network is computed.

    Input:
        connections (list): List of tuples representing the connections between vertices.
        maxIn (list): List of integers representing the maximum in capacity of each vertex.
        maxOut (list): List of integers representing the maximum out capacity of each vertex.
        origin (int): Integer representing the origin vertex.
        targets (list): List of integers representing the target vertices.

    Output:
        The maximum throughput of the network.

    Time complexity:
        Best:
            O(V * E^2) where V is the number of vertices and E is the number of edges

        Worst:
            O(V * E^2)    
    """
    # the number of vertices in the original network
    vertices = len(maxIn)

    # create the residual network
    network = ResidualNetwork(vertices)

    # split each vertex
    network.split_vertex(maxIn, maxOut)

    # create the residual network
    network.create_network(connections, is_residual = True)

    # add the super sink and connect it to the 'out' vertices of the target vertices to the super sink
    network.create_super_sink(targets)

    # add a super source and connect it to the 'in' vertices of the origin vertex to the super source
    network.create_super_source(origin, maxOut)

    return network.ford_fulkerson(network.super_source, network.super_sink)


# ==================== Q2 ====================

class Node:
    """
    Class representing a node in the Trie.
    
    Precondition:
        None
    Postcondition:
        A new instance of Node is created with the specified character. The node is initialized as a non-terminal node 
        (i.e., it does not complete a word), with no parent, no children, and no most frequent word.

    Input:
        char (str): The character stored in this node.
    Return:
        None

    Time complexity: 
        Best:
            O(1)
        Worst:
            O(1)
            
    Space complexity: 
        Input:
            O(1)
        Aux:
            O(1)
    """
    def __init__(self, char):
        self.char = char
        self.parent = None
        
        # it is 27 due to including the special character
        self.children = [None] * 27

        self.is_complete_word = False
        self.frequency_of_word = 0
        self.most_frequent_word = None

class CatsTrie:
    """
    Function Description:
        Initializes a new Trie with a root node and inserts the provided sentences into the Trie.
    
    Precondition:
        None
    Postcondition:
        A new instance of CatsTrie is created with a root node and all the sentences inserted into the Trie.

    Input:
        sentences (list of str): The list of sentences to be inserted into the Trie at initialization.
    Return:
        None

    Time complexity: 
        Best:
            O(NM) where n is the number of sentences and m is the number of characters in the longest sentence.
        Worst:
            O(NM)
            
    Space complexity: 
        Input:
            O(NM)
        Aux:
            O(NM)
    """
    def __init__(self, sentences):
        self.root = Node('')

        # insert all the sentences into the trie
        for sentence in sentences:
            self.insert(sentence)

    def get_ascii(self, char):
        """
        Function Description:
            Converts the given character into its corresponding ASCII value adjusted for our trie data structure.

        Precondition:
            char is a single character string and can be either a lower case letter or "$".

        Postcondition:
            Returns the corresponding index for the character based on its ASCII value. The '$' character is given an index of 0.

        Input:
            char (str): The character to be converted to its corresponding ASCII value.

        Return:
            int: The corresponding index of the character based on its ASCII value.

        Time complexity: 
            Best:
                O(1)
            Worst:
                O(1)

        Space complexity: 
            Input:
                O(1) 
            Aux:
                O(1)
        """
        return ord(char) - 96 if char != "$" else 0

    def insert(self, sentence):
        """
        Function Description:
            Inserts a sentence into the trie, creating nodes for each character in the sentence.

        Precondition:
            sentence is a string of lower case letters.

        Postcondition:
            The sentence is inserted into the trie, creating or traversing nodes as necessary, and the most frequent word of the nodes is updated.

        Input:
            sentence (str): The sentence to be inserted into the trie.

        Return:
            None

        Time complexity: 
            Best:
                O(M) where M is the length of the sentence.
            Worst:
                O(M)

        Space complexity: 
            Input:
                O(M) where M is the length of the sentence.
            Aux:
                O(1)
        """
        node = self.root

        # for each character in the sentence (appended with '$'), get its ascii value, but 
        # if a node corresponding to the character does not exist, create a new node.
        for char in f"{sentence}$":
            index = self.get_ascii(char)
            
            if not node.children[index]:
                node.children[index] = Node(char)
                node.children[index].parent = node
            node = node.children[index]

        # mark the last node as a complete word, update the frequency and update the most frequent word
        node.is_complete_word = True
        node.frequency_of_word += 1
        self.update_most_frequent_word(node, sentence)

    def update_most_frequent_word(self, node, sentence):
        """
        Function Description:
            Updates the most frequent word of the given node and all its parents.

        Precondition:
            node is an instance of Node, and sentence is a string of lower case letters.

        Postcondition:
            The most frequent word of the node and all its parents is updated according to the specified rules.

        Input:
            node (Node): The node whose most frequent word is to be updated.
            sentence (str): The sentence used for comparison when updating the most frequent word.

        Return:
            None

        Time complexity: 
            Best:
                O(N) where n is the number of parents of the node.
            Worst:
                O(N)

        Space complexity: 
            Input:
                O(1)
            Aux:
                O(1)
        """

        # the base case
        if node is None: 
            return
        
        # if the node's most frequent word is None or the frequency of the word is greater than the current most frequent word, or the frequency is the same but the sentence is lexicographically smaller, update the most frequent word
        if (
            node.most_frequent_word is None
            or node.frequency_of_word > node.most_frequent_word[1]
            or (
                node.frequency_of_word == node.most_frequent_word[1]
                and sentence < node.most_frequent_word[0]
            )
        ):
            node.most_frequent_word = (sentence, node.frequency_of_word)

        # recursively update the most frequent word of the parent node
        self.update_most_frequent_word(node.parent, node.most_frequent_word[0] if node.most_frequent_word else '')

    def find_most_frequent_word(self, node):
        """
        Function Description:
            Finds the most frequent word in the subtree rooted at the given node.

        Precondition:
            node is an instance of Node or None.

        Postcondition:
            Returns the most frequent word and its frequency in the subtree rooted at node, or None if no such word exists.

        Input:
            node (Node): The root of the subtree to search.

        Return:
            tuple: A tuple (most_frequent_word, frequency), or None if no such word exists.

        Time complexity: 
            Best:
                O(1) if the node has no children.
            Worst:
                O(N) where n is the number of children of the node.

        Space complexity: 
            Input:
                O(1)
            Aux:
                O(1)
        """
        # the base case
        if node is None:
            return None
        
        most_frequent_word = node.most_frequent_word

        # visit each child and update the most frequent word if a more frequent word is found.
        for child in node.children:
            child_word = self.find_most_frequent_word(child)
            if child_word is not None and (most_frequent_word is None or child_word[1] > most_frequent_word[1]):
                most_frequent_word = child_word

        return most_frequent_word

    def autoComplete(self, prompt):
        """
        Function Description:
            Auto-completes the given prompt to the most frequent word in the trie that starts with the prompt.

        Approach description: 
            The autoComplete function begins its process with a given prompt string as input. This string acts as a prefix, guiding the function to suggest the most frequently inserted word that starts with this prefix from the trie data structure.

            Starting from the root of the trie, the function navigates through the nodes that correspond to each character in the prompt string. This navigation is performed by mapping each character in the prompt to a child node of the current node, using the ASCII value of the character as the guiding parameter.

            The goal of the autoComplete function is to reach the node that represents the last character of the prompt. If it encounters a situation where the current node doesn't have a child node corresponding to the next character in the prompt, it understands that no word starting with this prompt exists in the trie. Consequently, it immediately returns None.

            However, if the function successfully navigates to the node that symbolizes the last character of the prompt, it indicates that at least one word beginning with the given prompt is present in the trie. The function then needs to identify the most frequent word among these. To achieve this, it invokes the find_most_frequent_word function, passing the current node as an argument.

            The find_most_frequent_word function's objective is to search the subtree rooted at the given node (including the node itself) for the most frequently inserted word. It initiates its process by considering the word represented by the current node (this could be None if the node doesn't represent a complete word) as the most frequent word. It then enters a recursive process where it calls itself for each child of the current node. If any of these recursive calls return a word that is more frequent than the current most frequent word, it promptly updates the most frequent word to the returned word. This iterative process continues until it has visited all children nodes, finally returning the most frequent word discovered.

            Upon receiving the output from the find_most_frequent_word function, the autoComplete function checks the returned value. If the returned value is a word, it confirms that the word is indeed the most frequent one starting with the given prompt, and returns this word as the auto-completion of the prompt. Conversely, if the returned value is None, it signifies that no complete word begins with the prompt in the trie, leading the autoComplete function to return None.
        
        Precondition:
            prompt is a string of lower case letters.

        Postcondition:
            Returns the most frequent word in the trie that starts with the prompt, or None if no such word exists.

        Input:
            prompt (str): The string to be auto-completed.

        Return:
            str: The most frequent word that starts with the prompt, or None if no such word exists.

        Time complexity: 
            Best:
                O(X + Y) where X is the length of the prompt and Y is the length of the most frequent sentence that begins with the prompt.
            Worst:
                O(n) where n is the number of nodes in the subtree rooted at the last character of the prompt.
            Special:
                If the word does not exist, the complexity is O(X), hence making it output-sensitive.
                
        Space complexity: 
            Input:
                O(1)
            Aux:
                O(X)  where X is the length of the prompt
        """
        node = self.root

        # loop over each character in the prompt to get their ascii value
        for char in prompt:
            index = self.get_ascii(char)

            # if the current node does not have a child corresponding to the next character in the prompt, exit and return none
            if node.children[index] is None:
                return None

            # otherwise, continue traversing the trie 
            node = node.children[index]

        # calculate the most frequent word
        most_frequent_word = self.find_most_frequent_word(node)

        # return the most frequent word if it exists, otherwise return None
        return most_frequent_word[0] if most_frequent_word else None