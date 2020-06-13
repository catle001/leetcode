from collections import deque


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return matrix

        directions = (0, 1), (0, -1), (1, 0), (-1, 0)
        row, col = len(matrix), len(matrix[0])
        p_set, a_set = set(), set()
        p_que, a_que = deque(), deque()
        result = []

        for i in range(row):
            p_que.append((i, 0))
            a_que.append((i, col - 1))
        for i in range(col):
            p_que.append((0, i))
            a_que.append((row - 1, i))

        while p_que:
            here = p_que.popleft()
            p_set.add(here)
            for direction in directions:
                i, j = here[0] + direction[0], here[1] + direction[1]
                if 0 <= i < row and 0 <= j < col and (i, j) not in p_set \
                        and matrix[i][j] >= matrix[here[0]][here[1]]:
                    p_que.append((i, j))

        while a_que:
            here = a_que.popleft()
            a_set.add(here)
            for direction in directions:
                i, j = here[0] + direction[0], here[1] + direction[1]
                if 0 <= i < row and 0 <= j < col and (i, j) not in a_set \
                        and matrix[i][j] >= matrix[here[0]][here[1]]:
                    a_que.append((i, j))

        for here in p_set:
            if here in a_set:
                result.append(here)

        return result


def main():
    matrix = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    solution = Solution().pacificAtlantic(matrix)
    print(solution)


if __name__ == '__main__':
    main()
