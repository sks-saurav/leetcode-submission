from collections import defaultdict
from typing import List

class Task:
    def __init__(self, taskId: int, taskDesc: str, dueDate: int):
        self.taskId = taskId
        self.taskDesc = taskDesc
        self.dueDate = dueDate
        self.isComplete = False

class User:
    def __init__(self, userId: int):
        self.userId = userId
        self.tasks = {}
        self.task_by_tag = defaultdict(list)

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
        ans = []
        # Use sorted() to avoid mutating the original lists passed into this method
        sorted_tasks = sorted(tasks, key=lambda x: x.dueDate)
        
        for t in sorted_tasks:
            if not t.isComplete:
                ans.append(t.taskDesc)

        return ans
        
    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        taskId = self._get_next_id()
        task = Task(taskId, taskDescription, dueDate)

        user = self._get_user(userId)
        user.tasks[taskId] = task

        # Use set(tags) to prevent duplicate tag entries for the same task
        for tag in set(tags):
            user.task_by_tag[tag].append(task)
            
        return taskId

    def getAllTasks(self, userId: int) -> List[str]:
        if userId not in self.users:
            return []

        tasks = list(self.users[userId].tasks.values())
        return self._extract_task(tasks)    

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        if userId not in self.users:
            return []

        user = self.users[userId]
        if tag in user.task_by_tag:
            tasks = user.task_by_tag[tag]
            return self._extract_task(tasks)
            
        return []    

    def completeTask(self, userId: int, taskId: int) -> None:
        if userId not in self.users:
            return

        user = self.users[userId]
        if taskId in user.tasks:
            user.tasks[taskId].isComplete = True