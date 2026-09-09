from typing import List
from sortedcontainers import SortedSet


class TaskManager:
  def __init__(self, tasks: List[List[int]]):
    # self.tasks stores: taskId -> (priority, userId)
    self.tasks = {}
    # (priority, taskId, userId)
    self.sl = SortedSet()

    for u, t, p in tasks:
      self.add(u, t, p)

  def add(self, userId: int, taskId: int, priority: int) -> None:
    self.tasks[taskId] = (priority, userId)
    self.sl.add((priority, taskId, userId))

  def edit(self, taskId: int, newPriority: int) -> None:
    old_p, uid = self.tasks[taskId]
    # Remove the exact old tuple in O(log N)
    self.sl.remove((old_p, taskId, uid))

    # Insert updated tuple in O(log N)
    self.tasks[taskId] = (newPriority, uid)
    self.sl.add((newPriority, taskId, uid))

  def rmv(self, taskId: int) -> None:
    p, uid = self.tasks.pop(taskId)
    # True O(log N) deletion
    self.sl.remove((p, taskId, uid))

  def execTop(self) -> int:
    if not self.sl:
      return -1

    # In ascending order, the maximum (highest priority, highest taskId)
    # is the last element at index -1
    priority, taskId, userId = self.sl.pop()  # O(log N)
    del self.tasks[taskId]

    return userId

# class Task:
#     def __init__(self, uid, tid, p):
#         self.uid = uid
#         self.tid = tid
#         self.p = p
#         self.active = True

#     def __lt__(self, other):
#         if self.p != other.p:
#             return self.p > other.p
#         return self.tid > other.tid
        
# class TaskManager:
#     def __init__(self, tasks: List[List[int]]):
#         self.tasks = {}
#         self.heap = []

#         for u,t,p in tasks:
#             self.add(u,t,p)

#     def add(self, userId: int, taskId: int, priority: int) -> None:
#         tt = Task(userId, taskId, priority)
#         self.tasks[taskId] = tt
#         heappush(self.heap, tt)

#     def edit(self, taskId: int, newPriority: int) -> None:
#         tt = self.tasks[taskId]
#         tt.active = False
#         self.add(tt.uid, taskId, newPriority)

#     def rmv(self, taskId: int) -> None:
#         tt = self.tasks[taskId]
#         tt.active = False
#         del self.tasks[taskId]

#     def execTop(self) -> int:
#         while len(self.heap) > 0:
#             tt = heappop(self.heap)
#             if tt.active:
#                 return tt.uid
                
#         return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()