class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        proc = []
        for val in arr:
            proc.append(val if len(proc) == 0 else proc[-1] ^ val)
        result = []
        for pair in queries:
            result.append(proc[pair[1]] if pair[0] == 0 else (proc[pair[1]] ^ proc[pair[0] - 1]))
        return result
