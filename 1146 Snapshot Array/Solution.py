class SnapshotArray:

    def __init__(self, length: int):
        self.index = 0
        self.changes = [{} for sub in range(length)]

    def set(self, index: int, val: int) -> None:
        self.changes[index][self.index] = val

    def snap(self) -> int:
        self.index += 1
        return self.index - 1

    def get(self, index: int, snap_id: int) -> int:
        def find_closest_lower(keys: list[int], target: int) -> int:
            keys.sort()

            # Looking for latest value
            if keys[-1] <= target:
                return keys[-1]
            # No change was made yet when snapshot was made
            if keys[0] > target:
                return -1

            left = 0
            right = len(keys) - 2
            while left < right:
                mid = left + (right - left) // 2
                if keys[mid] <= target and keys[mid + 1] > target:
                    return keys[mid]
                elif keys[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return keys[left]

        element_history = self.changes[index]

        # No change was made to this element
        if len(element_history) == 0:
            return 0

        # We have the exact snapshot
        if snap_id in element_history:
            return element_history[snap_id]

        # No snapshot of that moment. Have to look for latest previous change
        ids = list(element_history.keys())
        actual_snap_id = find_closest_lower(ids, snap_id)
        if actual_snap_id == -1:
            return 0
        return element_history[actual_snap_id]
