from collections import Counter


class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4

        counter = Counter(matchsticks)
        unique = list(counter.keys())
        unique.sort()
        print(counter)
        print(unique)
        print(target)

        if max(unique) > target:
            return False

        def backtrack(remainder: int, index: int):
            print(f"remainder: {remainder}, index: {index}")
            while index >= 0:
                print(f"unique[{index}]: {unique[index]}")
                print(f"counter[unique[{index}]]: {counter[unique[index]]}")
                if unique[index] > remainder or counter[unique[index]] <= 0:
                    index -= 1
                    print(f"Continue. New index: {index}")
                    continue
                remainder -= unique[index]
                counter[unique[index]] -= 1
                if remainder == 0:
                    return True
                if backtrack(remainder, index):
                    return True
                remainder += unique[index]
                counter[unique[index]] += 1
                index -= 1
            print("Retuning False")
            return False

        for i in range(4):
            if not backtrack(target, len(unique) - 1):
                return False

        return True
