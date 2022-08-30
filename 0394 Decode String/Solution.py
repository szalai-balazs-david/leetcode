class Solution:
    def decodeString(self, s: str) -> str:
        count = 0
        prefix = ""
        content = ""
        suffix = ""
        stage = 0 # 0: prefix, 1: count, 2: content, 3: done
        content_start = 0
        bracket_count = 0
        for i in range(len(s)):
            match stage:
                case 0:
                    if s[i].isdigit():
                        stage = 1
                        prefix = s[:i]
                        count = count * 10 + int(s[i])
                case 1:
                    if s[i] == '[':
                        stage = 2
                        content_start = i + 1
                        bracket_count += 1
                    else:
                        count = count * 10 + int(s[i])
                case 2:
                    if s[i] == '[':
                        bracket_count += 1
                    elif s[i] == ']':
                        bracket_count -= 1
                        if bracket_count == 0:
                            content = s[content_start : i]
                            content = self.decodeString(content)
                            suffix = self.decodeString(s[i+1:])
                            break

        if stage == 0:
            return s

        content = "".join([content for i in range(count)])
        return f"{prefix}{content}{suffix}"
