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
        conn = get_connection() 
        try: 
            cursor = conn.execute( 
                        """  
                        INSERT INTO tasks (title, done) 
                        VALUES (?, ?) 
                        """, 
                        (newtask.title, int(newtask.done)), 
                        ) 
            conn.commit() 
            
            return Task( 
                    id=cursor.lastrowid, 
                    title=newtask.title, 
                    done=newtask.done, 
                    ) 
        finally: 
            conn.close()
        
    
    def replace_task(self, id : int , update : UpdateTask) -> Task:   
        conn = get_connection()   
        try: 
            cursor = conn.execute("""  
                            UPDATE tasks 
                            SET title = ?, done = ? 
                            WHERE id = ?
                                  """,  
                            (update.title, int(update.done), id,), ) 
            if cursor.rowcount == 0: 
                raise LookupError("ID not found")  
            conn.commit() 
            
            return Task( 
                        id=id, 
                        title=update.title, 
                        done=update.done, 
                        )
        finally: 
            conn.close()
        
            
    def delete_task(self, id : int):   
        conn = get_connection()   
        try:  
            cursor = conn.execute( 
                        """ 
                        DELETE FROM tasks 
                        WHERE id = ? 
                        """, (id,),) 
            if cursor.rowcount == 0: 
                raise LookupError("ID not found") 
            conn.commit() 
        finally:  
            conn.close() 
            
            
            
    
    
    

    
