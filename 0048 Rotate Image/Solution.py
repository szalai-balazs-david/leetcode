class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        layers = int(len(matrix) / 2)
        center = layers

        for i in range(layers):
            if len(matrix) % 2 == 0:
                core = center - i - 1
                nCore = -(core + 1)
                for j in range(2 * i + 1):
                    pos = center + i - j
                    nPos = -(pos + 1)
                    matrix[core][pos], matrix[nPos][core], matrix[nCore][nPos], matrix[pos][nCore] = \
                        matrix[nPos][core], matrix[nCore][nPos], matrix[pos][nCore], matrix[core][pos]
            else:
                core = center - i - 1
                nCore = -(core + 1)
                for j in range(2 * (i + 1)):
                    pos = center + i - j
                    nPos = -(pos + 1)
                    matrix[core][pos], matrix[nPos][core], matrix[nCore][nPos], matrix[pos][nCore] = \
                        matrix[nPos][core], matrix[nCore][nPos], matrix[pos][nCore], matrix[core][pos]
