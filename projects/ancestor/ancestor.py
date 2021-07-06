

# we should use depth first search because we are traversing the entire tree before going down another tree


""""
In class solution
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def _init_(self):
        self.vertices= {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices(vertex_id)= set

    def add_edges(self, v1, v2):
        if v1 in self.vertices(v1) and v2 in self.vertices
            sekf,vertices(v1).add(v2)
        else:
            raise IndexError("That Vertex does not exist)
    def earliest_ancestor(ancestors, startin_Node):
        graph= Graph()
        for pair in ancestors:
            graph.add_vertex(pair[0])
            graph.add_vertex(pair[1])

            graph.add_edges(pair[1], pair[0])
        
        qq= Queue()
        qq.enqueue([startin_node])


        max_path_length = 1
        earliest_ancestor= -1

        while q.size() > 0:
            path.qq.dequeue()
            v= path[-1]

            if len(path) >= max_path_length and v < (earliest_ancestor) or (len(path)> max_pass_length):
                earliest_ancestor= v
                max_pass_length = len(path)
            for neighbor in graph.vertices[v]:
                path_copy = list(path)
                path.copy.append(neighbor)
                qq.enqueue(path_copy)
    return earliest_ancestor

"""


class Stack():
    def __init__(self):
        self.stack = []

    def add(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    graph = {}
    for pair in ancestors:
        if pair[1] in graph:
            graph[pair[1]].append(pair[0])
        else:
            graph[pair[1]] = [pair[0]]

    stack = Stack()
    visited = set()
    stack.add([starting_node])
    anc_len = 0

    if starting_node not in graph:
        return -1
    while stack.size() > 0:
        path = stack.pop()
        node = path[-1]
        if node in graph:
            for parent in graph[node]:
                new_path = list(path)
                new_path.append(parent)
                stack.add(new_path)

                """ """
                #if len(new_path) > 0:
                 #   starting_node = min(starting_node, parent)#
                elif len(new_path) > anc_len:
                    starting_node = parent
                    anc_len = len(new_path)
    return starting_node
