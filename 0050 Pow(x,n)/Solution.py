class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        result = 1
        dict = {}
        if n > 0:
            m = 1
            dict[m] = x
            while 2 * m < n:
                dict[2 * m] = dict[m] * dict[m]
                m = 2 * m
            keys = list(dict.keys())
            while n > 0:
                k = 1
                for key in keys:
                    if k < key < n:
                        k = key
                result = result * dict[k]
                n -= k
        else:
            m = -1
            dict[m] = 1 / x
            while 2 * m > n:
                dict[2 * m] = dict[m] * dict[m]
                m = 2 * m
            keys = list(dict.keys())
            print(dict)
            while n < 0:
                k = -1
                for key in keys:
                    if k > key > n:
                        k = key
                result = result * dict[k]
                n -= k
        return result
