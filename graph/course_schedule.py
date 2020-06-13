import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        graph = {}
        dp = {}
        num_course_aval = 0
        for course_prerequisite in prerequisites:
            course, pre_course = course_prerequisite[0], course_prerequisite[1]
            if pre_course not in graph:
                graph[pre_course] = []
            if course not in graph:
                graph[course] = [pre_course]
            else:
                graph[course].append(pre_course)
        for course in graph:
            if not self.can_finish_util(course, graph, dp, set()):
                return False
        return True

    def can_finish_util(self, course, graph, dp, visited):
        if course in dp:
            return dp[course]
        for pre_course in graph[course]:
            if pre_course not in visited:
                visited.add(pre_course)
                if not self.can_finish_util(pre_course, graph, dp, visited):
                    dp[course] = False
                    return False
                visited.remove(pre_course)
            else:
                dp[course] = False
                return False
        dp[course] = True
        return True

    def canFinish2(self, numCourses, prerequisites): #topological sort
        dic2 = collections.defaultdict(list)
        numPrior = [0 for _ in range(numCourses)]

        for s, e in prerequisites:
            dic2[e].append(s)
            numPrior[s] += 1

        start = [s for s in range(numCourses) if numPrior[s] == 0]

        for c in start:
            for p in dic2[c]:
                numPrior[p] -= 1
                if numPrior[p] == 0:
                    start.append(p)
        return len(start) == numCourses


def main():
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    prerequisites = [[1, 2], [1, 3], [2, 3]]
    solution = Solution().canFinish(numCourses, prerequisites)
    print(solution)


if __name__ == '__main__':
    main()