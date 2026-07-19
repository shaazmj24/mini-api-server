from abc import ABC , abstractmethod 
from app.models import UpdateTask, NewTask, Task

class TaskRepository(ABC): 
    @abstractmethod 
    def list_tasks(self) -> list[Task]: 
        pass   
    
    @abstractmethod
    def get_task(self, id : int) -> Task:
        pass
    
    @abstractmethod 
    def add_task(self, task: NewTask) -> Task: 
        pass 
    
    @abstractmethod 
    def replace_task(self, id : int , update: UpdateTask) -> Task: 
        pass
    
    @abstractmethod 
    def delete_task(self, id: int) -> None: 
        pass
    
    
    
    

