from fastapi import FastAPI 
from fastapi.responses import JSONResponse

tasks = [
    {"id": 1, "title": "Practice leetcode", "Done" : True}, 
    {"id": 2, "title": "Uni Registration", "Done" : False}, 
    {"id": 3, "title": "Grocery", "Done" : True}
    ]

app = FastAPI() 

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

