from collections import defaultdict

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(defaultdict)
        price = {}
        for start, end, weight in flights:
            graph[start][end] = weight
        this = src
        for next in graph[src]:
            if next not in price:
                price[next] =




def main():
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    solution = Solution().findCheapestPrice(n, edges, src, dst, k)
    print(solution)


if __name__ == '__main__':
    main()