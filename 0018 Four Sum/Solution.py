class Solution:
    # [-2,-1,0,0,1,2]
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        return self.nSum(nums, target, 4)

    def nSum(self, nums: list[int], target: int, count: int) -> list[list[int]]:
        if len(nums) < count:
            return []

        if count == 2:
            print(f"TwoSum for: {nums} and {target}")
            sub_result = []
            l = 0
            r = len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    sub_result.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    r -= 1
            result = []
            for x in sub_result:
                if not result.__contains__(x):
                    result.append(x)
            return result
        else:
            print(f"NSum for: {nums} and {target}, count = {count}")
            sub_result = []
            for i in range(len(nums) - count + 1):
                res = self.nSum(nums[i + 1:], target - nums[i], count - 1)
                for x in res:
                    x.insert(0, nums[i])
                    sub_result.append(x)
            result = []
            for x in sub_result:
                if not result.__contains__(x):
                    result.append(x)
            return result
