class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add(c1: chr, c2: chr, remainder: bool) -> (chr, bool):
            val = 1 if remainder else 0
            remainder = False
            result = '0'
            if c1 == '1':
                val += 1
            if c2 == '1':
                val += 1

            match val:
                case 0:
                    result = '0'
                case 1:
                    result = '1'
                case 2:
                    result = '0'
                    remainder = True
                case 3:
                    result = '1'
                    remainder = True

            return result, remainder

        result = ""
        remainder = False

        is_a_long = len(a) > len(b)
        long = a if is_a_long else b
        short = b if is_a_long else a
        diff = len(long) - len(short)
        for i in range(len(long) - 1, -1, -1):
            short_c = short[i - diff] if i - diff >= 0 else '0'
            c, remainder = add(long[i], short_c, remainder)
            result += c

        if remainder:
            result += '1'
        result = result[::-1]
        return result
