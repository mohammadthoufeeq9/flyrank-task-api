from fastapi import FastAPI
from fastapi import HTTPException,status
from pydantic import BaseModel


app=FastAPI()


class Taskcreate(BaseModel):
    title:str


class TaskUpdate(BaseModel):
    title:str|None=None
    done:bool|None=None

@app.get("/")
def root():
    return{
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def healthcheck():
    return{
        "Status":"Ok",
        "Message":"Api is running"
    }


tasks=[{"id": 1, "title": "Learn boxing", "done": False},
       {"id": 2, "title": "Learn kunfu", "done": False}]

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/task/{task_id}")
def get_task_by_id(task_id:int):
    for task in tasks:
        if task["id"] == task_id:
            return task
        else:
            return {
                HTTPException(detail="Enter a valid task_id",status_code=status.HTTP_404_NOT_FOUND)
            }

@app.post("/task-add")
def task_add(task:Taskcreate):
    if not task.title.strip():
        raise HTTPException(detail="Title cannot be empty",status_code=status.HTTP_400_BAD_REQUEST)
    new_id=max((t["id"] for t in tasks),default=0)+1
    new_task=(
        {"id": new_id, "title": task.title, "done": False}
    )

    tasks.append(new_task)

    return new_task

@app.put("/task/{task_id}")
def task_update(task_id:int,task:TaskUpdate):
    if not task.title.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Tittle cannot be empty")
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = task.title
            t["done"] = task.done
            return t
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    