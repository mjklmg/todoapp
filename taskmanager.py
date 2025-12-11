import json
import os
from dataclasses import  dataclass
import datetime

@dataclass
class Task:

    id: int
    title: str
    status: str
    created_at: str
    updated_at: str

    def toDict(self):
        return self.__dict__
#klasa task manager z obsluga CRUD
class TaskManager:
    def __init__(self):
        self._tasks = []
        self.next_id = 1

    def add_task(self, title):
        t = Task(self.next_id, title, "todo", datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat())
        self._tasks.append(t)
        self.next_id+=1
        return t


    def save_tasks(self, file):
        with open(file, "w") as f:
            json.dump([t.toDict() for t in self._tasks], f)

    def read_tasks(self, file):
        self._tasks = []

        if not os.path.exists(file) or os.path.getsize(file) == 0:
            self.next_id = 1
            return

        with open(file, "r") as f:
            data = json.load(f)
        max_id = 0

        for t in data:
            if t["id"] > max_id:
                max_id = t["id"]
            self._tasks.append(Task(t["id"], t["title"], t["status"], t["created_at"], t["updated_at"]))
        self.next_id = max_id+1

    def update_task(self, id, titleN):
        for t in self._tasks:
            if t.id == id:
                t.title = titleN
                t.updated_at = datetime.datetime.now().isoformat()
                return True
        return False

    def delete_task(self, id):
        for index, task in enumerate(self._tasks):
            if task.id == id:
                del self._tasks[index]
                return True
        return False

    def list_all(self, file, status=None):
        self.read_tasks(file)
        was_found = 0
        for t in self._tasks:
            if  status is None or t.status == status:
                was_found+=1
                print(f"[{t.id}] | {t.title} | {t.status}")
        if was_found==0: print("none tasks have been found.")

    def change_status(self, file, id, status):
        self.read_tasks(file)
        for t in self._tasks:
            if t.id == id:
                t.status = status
                return True
        return False
