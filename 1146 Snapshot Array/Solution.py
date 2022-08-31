import bisect


class SnapshotArray:

    # Cheated. Looked at solution. But this bisect is helpful!
    def __init__(self, length: int):
        self.index = 0
        self.changes = [[[-1, 0]] for i in range(length)]

    def set(self, index: int, val: int) -> None:
        self.changes[index].append([self.index, val])

    def snap(self) -> int:
        self.index += 1
        return self.index - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.changes[index], [snap_id + 1]) - 1
        return self.changes[index][i][1]
