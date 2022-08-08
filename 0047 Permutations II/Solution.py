class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:

        def backtrack(seq: list[int], result: list[list[int]], rest: list[int]):
            if len(rest) == 0:
                result.append(list(seq))
                return

            for i in range(len(rest)):
                if i != rest.index(rest[i]):
                    continue
                val = rest[i]
                seq.append(val)
                del rest[i]
                backtrack(seq, result, rest)
                seq.pop()
                rest.insert(i, val)

        nums.sort()
        results = []
        seq = []

        backtrack(seq, results, nums)

        return results
