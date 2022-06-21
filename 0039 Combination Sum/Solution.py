class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()

        for i in range(len(candidates)):
            candidate = candidates[i]
            if candidate > target:
                continue
            if candidate == target:
                result.append([candidate])
            else:
                sub_results = self.combinationSum(candidates[i:], target - candidate)
                for sub_result in sub_results:
                    sub_result.append(candidate)
                    sub_result.sort()
                    if sub_result not in result:
                        result.append(sub_result)

        return result
