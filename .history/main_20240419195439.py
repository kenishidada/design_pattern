
# FacadePattern
class Solution:
    def __init__(self):
        pass

    def solve(self, n: int) -> int:
        return n

class Solution2:
    def __init__(self):
        pass

    def solve(self, n: int) -> int:
        return n

class Solution3:
    def __init__(self):
        pass

    def solve(self, n: int) -> int:
        return n


class FacadeSolution:
    def __init__(self):
        self.solution1 = Solution()
        self.solution2 = Solution2()
        self.solution3 = Solution3()

    def solve(self, n: int) -> int:
        return self.solution1.solve(n) + self.solution2.solve(n) + self.solution3.solve(n)

facade = FacadeSolution()
print(facade.solve(10))

