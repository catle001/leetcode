from collections import deque, defaultdict


class Graph():
    def __init__(self, length):
        self.len = length
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        # Add w to v ist.
        self.graph[v].append(w)
        # Add v to w list.
        self.graph[w].append(v)


def is_tree(graph):
    if not graph.len:
        return True
    visited = set()
    queue = deque()
    queue.append((0, None))
    while queue:
        node, parent = queue.popleft()
        if node in visited:
            return False
        else:
            visited.add(node)
        for child in graph.graph[node]:
            if child != parent:
                queue.append((child, node))
    return len(visited) == graph.len


def main():
    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)

    g2 = Graph(5)
    g2.addEdge(1, 0)
    g2.addEdge(0, 2)
    g2.addEdge(2, 1)
    g2.addEdge(0, 3)
    g2.addEdge(3, 4)

    print is_tree(g1)
    print is_tree(g2)


if __name__ == '__main__':
    main()