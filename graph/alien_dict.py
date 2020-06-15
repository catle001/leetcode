def char_order(words):
    if len(words) == 1:
        return [char for char in words[0]]
    graph = create_graph(words)
    stack = []
    visited = set()
    for key in graph:
        if key not in visited:
            topo_sort(key, graph, stack, visited)
    stack.reverse()
    return stack


def topo_sort(key, graph, stack, visited):
    visited.add(key)
    for next in graph[key]:
        if next not in visited:
            topo_sort(next, graph, stack, visited)
    stack.append(key)


def create_graph(words):
    graph = {}
    for i in range(len(words) - 1):
        word, next = words[i], words[i + 1]
        for w in word, next:
            for char in w:
                if char not in graph:
                    graph[char] = []
        for j in range(min(len(word), len(next))):
            char, next_char = word[j], next[j]
            if char != next_char:
                graph[char].append(next_char)
                break
    return graph


def main():
    words = ["baa", "abcd", "abca", "cab", "cad"]
    words = ["caa", "aaa", "aab"]
    words = []
    words = ["sdfgh"]
    words = ["caa", "aaa"]
    solution = char_order(words)
    print(solution)


if __name__ == '__main__':
    main()
