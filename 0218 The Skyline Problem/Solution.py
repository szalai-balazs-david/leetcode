from queue import PriorityQueue


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        class Point:
            def __init__(self, x: int):
                self.x = x
                self.y = []
                self.is_start = []

            def __lt__(self, other):
                return self.x < other.x

            def add(self, height: int, start: bool):
                self.y.append(height)
                self.is_start.append(start)

        if buildings is None or len(buildings) == 0:
            return []

        dict = {}
        for building in buildings:
            if building[0] not in dict:
                dict[building[0]] = Point(building[0])
            dict[building[0]].add(building[2], True)
            if building[1] not in dict:
                dict[building[1]] = Point(building[1])
            dict[building[1]].add(building[2], False)

        q = PriorityQueue()

        for key in dict:
            q.put(dict[key])

        result = []
        active_buildings = []
        highest = 0

        while not q.empty():
            point = q.get()
            for i in range(len(point.y)):
                if point.is_start[i]:
                    active_buildings.append(point.y[i])
                else:
                    active_buildings.remove(point.y[i])

            new_highest = 0 if len(active_buildings) == 0 else max(active_buildings)
            if highest != new_highest:
                result.append([point.x, new_highest])
                highest = new_highest

        return result
