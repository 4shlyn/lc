class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        visited = set()
        visited.add(0)
        q = deque()
        for key in rooms[0]:
            q.append(key)

        while q:
            room = q.popleft()
            if room in visited:
                continue
            visited.add(room)
            for k in rooms[room]:
                q.append(k)
            if len(visited) == n:
                return True
        if len(visited) == n:
                return True
        return False

    