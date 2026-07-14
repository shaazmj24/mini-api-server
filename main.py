from fastapi import FastAPI 
from fastapi.responses import JSONResponse 
from pydantic import BaseModel 

tasks = [
    {"id": 1, "title": "Practice leetcode", "done" : True}, 
    {"id": 2, "title": "Uni Registration", "done" : False}, 
    {"id": 3, "title": "Grocery", "done" : True}
    ]

app = FastAPI()  

class newTask(BaseModel):  
    title : str | None = None 

@app.get("/") 
def root():  
    ms = { 
          "name": "Task API", 
          "version": "1.0", 
          "endpoints": ["/tasks"]  
          } 
    return ms 

@app.get("/health") 
def health(): 
    return {"status" : "ok"}

@app.get("/tasks")    
def get_tasks(): 
    return tasks 

@app.get("/tasks/{id}") 
def get_task(id : int):    
    for t in tasks: 
        if t["id"] == id: 
            return t   
         
    return JSONResponse(
        status_code=404, 
        content={"error" : f"Task {id} not found"}
    )

@app.post("/tasks") 
def add_new_task(new_task : newTask): 
    if new_task.title is None or new_task.title.strip() == "":   
        return JSONResponse( 
                        status_code=400,  
                        content={"bad request" : "Title cannot be empty"}  
                        )  
        
    new_task = {"id" : tasks[-1]["id"] + 1 , "title" : new_task.title, "done" : False} 
    tasks.append(new_task)  
    
    return JSONResponse(
        status_code= 201, 
        content=new_task 
    )
    
    



