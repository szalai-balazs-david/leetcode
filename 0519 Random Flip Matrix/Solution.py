import random


class Solution:

    # Cheated. Looked at solution
    def __init__(self, m: int, n: int):
        self.column_count = n
        self.redirects = {}
        self.end = m * n - 1
        self.start = 0

    def flip(self) -> list[int]:
        rand = random.randint(self.start, self.end)
        result = self.redirects.get(rand, rand)
        self.redirects[rand] = self.redirects.get(self.start, self.start)
        self.start += 1
        return divmod(result, self.column_count)

    def reset(self) -> None:
        self.redirects = {}
        self.start = 0
