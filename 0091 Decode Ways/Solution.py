class Solution:
    def numDecodings(self, s: str) -> int:
        def is_valid(chars: str) -> bool:
            match len(chars):
                case 1:
                    return chars != "0"
                case 2:
                    match chars[0]:
                        case '1':
                            return True
                        case '2':
                            return chars[1] in "0123456"
                    return False
            return False

        def is_valid_char(c: chr) -> bool:
            return c != '0'

        def is_valid_pair(chars: str) -> bool:
            match chars[0]:
                case '1':
                    return True
                case '2':
                    return chars[1] in "0123456"
            return False

        def charDecodings(chars: str) -> int:
            match len(chars):
                case 1:
                    return 1 if is_valid(chars) else 0
                case 2:
                    result = 0
                    if is_valid(chars):
                        result += 1
                    if is_valid(chars[0]) and is_valid(chars[1]):
                        result += 1
                    return result
            return 0

        if len(s) == 1:
            return charDecodings(s)

        results = [charDecodings(s[0]), charDecodings(s[:2])]
        for i in range(2, len(s)):
            x = 0
            if is_valid_char(s[i]):
                x += results[-1]
            if is_valid_pair(s[i-1:i+1]):
                x += results[-2]
            if x == 0:
                return 0
            results.append(x)
        return results[-1]


