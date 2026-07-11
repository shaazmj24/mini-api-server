from fastapi import FastAPI 
import random 

app = FastAPI() 

@app.get("/") 
def hello_world(): 
    return {"message": "hello world"} 

@app.get("/random")   
def random_num():   
    num = random.randint(1, 11)
    return {"Random number" : num}

