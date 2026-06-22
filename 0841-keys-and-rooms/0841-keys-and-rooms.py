class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        open_room = [0]
        visited = [False] * n

        while open_room:
            new_room_unlocked = []

            while open_room:
                r = open_room.pop()
                if not visited[r]:
                    visited[r] = True
                    new_room_unlocked += rooms[r]

            open_room += new_room_unlocked

        return all(visited)
            

