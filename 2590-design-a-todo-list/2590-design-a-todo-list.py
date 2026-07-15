import bisect
from collections import defaultdict
from typing import List

class Task:
    def __init__(self, taskId: int, taskDesc: str, dueDate: int):
        self.taskId = taskId
        self.taskDesc = taskDesc
        self.dueDate = dueDate
        self.isComplete = False
        
    # This allows bisect to automatically sort Task objects by dueDate
    def __lt__(self, other):
        return self.dueDate < other.dueDate

class User:
    def __init__(self, userId: int):
        self.userId = userId
        self.tasks_map = {}                      # O(1) lookup for completeTask
        self.all_tasks = []                      # Maintained as a sorted list
        self.task_by_tag = defaultdict(list)     # Maintained as sorted lists

class TodoList:
    def __init__(self):
        self.id = 0
        self.users = {}
    
    def _get_user(self, userId: int) -> User:
        if userId not in self.users:
            self.users[userId] = User(userId)
        return self.users[userId]

    def _get_next_id(self) -> int:
        self.id += 1
        return self.id

    def _extract_task(self, tasks: List[Task]) -> List[str]:
        # NO SORTING HERE ANYMORE! Just a fast O(N) extraction.
        return [t.taskDesc for t in tasks if not t.isComplete]

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        taskId = self._get_next_id()
        task = Task(taskId, taskDescription, dueDate)

        user = self._get_user(userId)
        user.tasks_map[taskId] = task
        
        # Insert into the main sorted list
        bisect.insort(user.all_tasks, task)

        # Insert into the tagged sorted lists
        for tag in set(tags):
            bisect.insort(user.task_by_tag[tag], task)
            
        return taskId

    def getAllTasks(self, userId: int) -> List[str]:
        if userId not in self.users:
            return []

        return self._extract_task(self.users[userId].all_tasks)    

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        if userId not in self.users:
            return []

        user = self.users[userId]
        return self._extract_task(user.task_by_tag.get(tag, []))    

    def completeTask(self, userId: int, taskId: int) -> None:
        if userId not in self.users:
            return

        user = self.users[userId]
        if taskId in user.tasks_map:
            user.tasks_map[taskId].isComplete = True