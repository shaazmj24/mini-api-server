from fastapi import FastAPI 
from fastapi.responses import JSONResponse , Response
from pydantic import BaseModel 

tasks = [
    {"id": 1, "title": "Practice leetcode", "done" : True}, 
    {"id": 2, "title": "Uni Registration", "done" : False}, 
    {"id": 3, "title": "Grocery", "done" : True}
    ]

app = FastAPI()  

class newTask(BaseModel):                 #data validation and serialization
    title : str | None = None 

class UpdateTask(BaseModel):
    title: str | None = None
    done: bool | None = None


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
        
    new_task = {"id" : max((task["id"] for task in tasks), default=0) + 1 , "title" : new_task.title, "done" : False} 
    tasks.append(new_task)  
    
    return JSONResponse(
        status_code= 201, 
        content=new_task 
    )
    
@app.put("/tasks/{id}") 
def replace_task(id : int, update: UpdateTask):    
    if update.title is None and update.done is None: 
        return JSONResponse(
            status_code=400,
            content={"error": "Provide title or done"}
        ) 
    
    if update.title is not None and update.title.strip() == "": 
        return JSONResponse(
            status_code=400,
            content={"error": "Title cannot be empty"}
        ) 
    task = None 
    for t in tasks: 
        if t["id"] == id:  
            task = t 
            break 
    
    if task is None:   
        return JSONResponse( 
                    status_code=404, 
                    content={"error": f"Task {id} not found"}   
                    )  
    if update.title is not None: 
        task["title"] = update.title 
    if update.done is not None: 
        task["done"] = update.done 
    
    return task 
    

@app.delete("/tasks/{id}") 
def delete_task(id : int):    
    task = None 
    for t in tasks: 
        if t["id"] == id:  
            tasks.remove(t) 
            return Response(status_code=204) 
    
    return JSONResponse(  
                status_code=404,  
                content={"error": f"Task {id} not found"}   
                )  

    

