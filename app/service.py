from app.models import Task, NewTask, UpdateTask
from app.repository.interface import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def list_tasks(self) -> list[Task]:
        return self.repository.list_tasks() 
    
    def get_task(self, id : int) -> Task: 
        return self.repository.get_task(id)

    def add_task(self, task: NewTask) -> Task:
        return self.repository.add_task(task)   
    
    def replace_task(self, id : int , update: UpdateTask) -> Task: 
        return self.repository.replace_task(id, update) 
    
    def delete_task(self, id : int) -> None: 
        self.repository.delete_task(id) 


    
    
    