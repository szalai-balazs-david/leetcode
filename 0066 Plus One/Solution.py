class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        digits[-1] = 0

        for i in range(len(digits) - 2, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        digits.insert(0, 1)

        return digits
