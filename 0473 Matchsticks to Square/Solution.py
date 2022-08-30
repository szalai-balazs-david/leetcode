from collections import Counter


class Solution:
    def __init__(self):
        self.skips = 0

    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4

        counter = Counter(matchsticks)
        unique = list(counter.keys())
        unique.sort()

        if max(unique) > target:
            return False

        def backtrack(remainder: int, index: int) -> bool:
            while index >= 0:
                if unique[index] > remainder or counter[unique[index]] <= 0:
                    index -= 1
                    continue
                remainder -= unique[index]
                counter[unique[index]] -= 1
                if remainder == 0:
                    if self.skips == 0:
                        return True
                    self.skips -= 1
                    remainder += unique[index]
                    counter[unique[index]] += 1
                    return False
                if backtrack(remainder, index):
                    return True
                remainder += unique[index]
                counter[unique[index]] += 1
                index -= 1
            return False

        skip_counter = 0
        while True:
            success = True
            self.skips = skip_counter
            counter = Counter(matchsticks)
            for i in range(4):
                print(counter)
                if not backtrack(target, len(unique) - 1):
                    success = False
                    break
            if success:
                return True
            if self.skips != 0:
                return False
            skip_counter += 1
