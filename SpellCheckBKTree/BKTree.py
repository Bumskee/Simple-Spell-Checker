from collections import deque

class BKTree:
    def __init__(self, distance_func):
        self._tree = None
        self._distance_func = distance_func

    def add(self, node):
        if self._tree is None:
            self._tree = (node, {})
            return

        current, children = self._tree
        while True:
            dist = self._distance_func(node, current, len(node), len(current))
            target = children.get(dist)
            if target is None:
                children[dist] = (node, {})
                break
            current, children = target

    def search(self, node, radius):
        found = False
        if self._tree is None:
            return []

        candidates = deque([self._tree])
        result = []
        while candidates:
            candidate, children = candidates.popleft()
            dist = self._distance_func(node, candidate, len(node), len(candidate))

            if dist == 0:
                found = True
            if dist <= radius:
                result.append((dist, candidate))

            low, high = dist - radius, dist + radius
            candidates.extend(c for d, c in children.items() if low <= d <= high)
        return result, found

if __name__ == '__main__':
    BKTree