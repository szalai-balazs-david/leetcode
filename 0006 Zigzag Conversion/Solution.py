class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows < 2):
            return s
        rows = []
        l = len(s)
        for i in range(numRows):
            rows.append("")
        char_per_group = numRows * 2 - 2
        for i in range(int(len(s) / char_per_group) + 1):
            for r in range(numRows):
                zig_char_index = char_per_group * i + r
                if zig_char_index < l:
                    rows[r] += s[zig_char_index]
                if r != 0 and r != numRows - 1:
                    zag_char_index = char_per_group * i + r + char_per_group - 2 * r
                    if zag_char_index < l:
                        rows[r] += s[zag_char_index]
        result = ""
        for r in rows:
            result += r
        return result
