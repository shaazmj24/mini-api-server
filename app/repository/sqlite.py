from app.repository.interface import TaskRepository , Task , UpdateTask , NewTask 
from app.database1 import get_connection

class SQLiteTaskRepository(TaskRepository): 
    def list_tasks(self) -> list[Task]: 
        conn = get_connection()    
        try: 
            rows = conn.execute( 
                                """  
                                SELECT id, title, done FROM tasks
                                """).fetchall() 
            return  [  
                Task( 
                     id=row["id"],  
                     title=row["title"], 
                     done=bool(row["done"]), 
                     )  
                    for row in rows 
                ] 
        finally: 
            conn.close() 
        
    
    def get_task(self, id : int) -> Task:    
        conn = get_connection()
        try: 
            row = conn.execute(
                """   
                SELECT id, title, done FROM tasks 
                WHERE id = ?
                """ , (id,),  
                ).fetchone() 
            if row is None: 
                raise LookupError("ID not found") 
            
            return Task(
                id=row["id"], 
                title=row["title"], 
                done=bool(row["done"]), 
            )
        finally: 
            conn.close() 
            
            
            

    def add_task(self, newtask: NewTask) -> Task:   
        pass 
        
    
    def replace_task(self, id : int , update : UpdateTask) -> Task:    
        pass 
        
            
    def delete_task(self, id : int):  
        pass 
    
    
    

    
