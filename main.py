from fastapi import FastAPI 

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
def health_s(): 
    return {"status" : "ok"}
