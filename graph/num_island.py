from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        directions = (0, 1), (0, -1), (1, 0), (-1, 0)
        num_island = 0
        visited = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    num_island += 1
                    queue = deque()
                    queue.append((i, j))
                    while queue:
                        here = queue.popleft()
                        for d in directions:
                            x, y = here[0] + d[0], here[1] + d[1]
                            if 0 <= x < row and 0 <= y < col and (x, y) not in visited \
                                and grid[x][y] == "1":
                                queue.append((x, y))
                                visited.add((x, y))
        return num_island


def main():
    matrix = [
        "11000",
        "11000",
        "00100",
        "00011"
    ]
    solution = Solution().numIslands(matrix)
    print(solution)


if __name__ == '__main__':
    main()