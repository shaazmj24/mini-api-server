from app.repository.interface import TaskRepository , Task , UpdateTask , NewTask

class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self.tasks: list[Task] = []
        self.next_id = 1

    def list_tasks(self) -> list[Task]:
        return self.tasks 
    
    def get_task(self, id : int) -> Task:   
        for t in self.tasks:  
            if t.id == id: 
                return t    
        
        raise LookupError("ID not found")

    def add_task(self, newtask: NewTask) -> Task:  
        new_task = Task(
            id=self.next_id,
            title=newtask.title, 
            done=newtask.done
        )
        self.tasks.append(new_task)
        self.next_id += 1   
        
        return new_task
        
    
    def replace_task(self, id : int , update : UpdateTask) -> Task:    
        for t in self.tasks:  
            if t.id == id: 
                t.title = update.title 
                if update.done is not None: 
                    t.done = update.done 
                return t 
        raise LookupError("ID not found")
        
            
    def delete_task(self, id : int):  
        for t in self.tasks: 
            if t.id == id: 
                self.tasks.remove(t) 
                return 
        
        raise LookupError("ID not found")
    

    

    