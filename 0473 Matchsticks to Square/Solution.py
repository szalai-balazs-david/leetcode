from collections import Counter


class Solution:
    def __init__(self):
        self.skips = 0

    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)
        # If not divisible by 4, then it can't be done
        if total % 4 != 0:
            return False
        target = total // 4

        counter = Counter(matchsticks)
        unique = list(counter.keys())
        unique.sort()

        # If any matchstick is longer than the target, then it can't be done
        if max(unique) > target:
            return False

        def backtrack(remainder: int, index: int) -> bool:
            while index >= 0:
                # Optimization option:
                # Instead of 1-by-1 decrement, it could binary search for first element where `unique[index] > remainder`
                # Not relevant as max matchstick count is only 15
                if unique[index] > remainder or counter[unique[index]] <= 0:
                    index -= 1
                    continue
                remainder -= unique[index]
                counter[unique[index]] -= 1
                if remainder == 0:
                    # A fully assembled side is created.
                    # If no skips are left, return True.
                    # If there are skips left, decrement available skips count and return False
                    # Optimization option:
                    # Save the state where we found the correct solution to avoid redoing work.
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

        # Skip counter is a protection mechanism.
        # The backtracking works on a per side basis.
        # The issue is that a side might be possible to assemble in multiple ways, and the one we find first might make the rest non-solvable.
        # See test case 4:
        # 13+11+1, 9+8+8 work, but then the other 2 sides can not be done.
        # 13+6+6, 11+7+7, 9+8+8, 8+8+8+1 works instead
        # The idea with skipping is that we skip the first <skip_counter> solutions.
        # Example:
        # skip_counter = 0 --> 13+11+1 and 9+8+8 are found, but then the 3rd side returns fail
        # skip_coutner = 1 --> 13+11+1 is skipped, and the next solution is found: 13+6+6. Then the algorithm can find the correct solution.
        # If not all skip options are exhausted by the end, then adding more skips does not help and we can return False
        skip_counter = 0
        while True:
            success = True
            # Globally available skip counter. This is manipulated inside the backtracking
            self.skips = skip_counter
            counter = Counter(matchsticks)
            # Try to assemble 4 sides of length <target> one-by-one
            for i in range(4):
                if not backtrack(target, len(unique) - 1):
                    success = False
                    break
            if success:
                return True
            # If not all skips are exhausted, there's no solution to be found. Return False
            if self.skips != 0:
                return False
            # Make another attempt with higher skip count. Maybe another solution exists
            skip_counter += 1
