from fastapi import FastAPI,Depends
from fastapi import HTTPException,status
from schema.schemas import Taskcreate,TaskUpdate
from database.database import get_db
from sqlalchemy.orm import Session
from database.models import Task

app=FastAPI()


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


# tasks=[{"id": 1, "title": "Learn boxing", "done": False},
#        {"id": 2, "title": "Learn kunfu", "done": False}]

@app.get("/tasks")
def get_tasks(db:Session=Depends(get_db)):
    task=db.query(Task).all()
    return task

@app.get("/task/{task_id}")
def get_task_by_id(task_id:int,db=Depends(get_db)):
    for task in db:
        if task["id"] == task_id:
            return task
        else:
            return {
                HTTPException(detail="Enter a valid task_id",status_code=status.HTTP_404_NOT_FOUND)
            }

@app.post("/task-add")
def task_add(task:Taskcreate,db:Session=Depends(get_db)):
    if not task.title.strip():
        raise HTTPException(detail="Title cannot be empty",status_code=status.HTTP_400_BAD_REQUEST)
    new_task=Task(title=task.title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.put("/task/{task_id}")
def task_update(task_id:int,task:TaskUpdate,db:Session=Depends(get_db),):
    task_obj=db.query(Task).filter(Task.id==task_id).first()
    if not task_obj:
        raise HTTPException(detail=f"No task with the {task_id}, Enter a valid id.",status_code=status.HTTP_404_NOT_FOUND)
    task_obj.title= task.title
    task_obj.done= task.done
    db.commit()
    db.refresh(task_obj)
    return task_obj


@app.delete("/task/{task_id}")
def del_task(task_id:int,db:Session=Depends(get_db)):
    task_obj=db.query(Task).filter(Task.id == task_id).first()
    if not task_obj:
        raise HTTPException(detail="oops! Tryagain-thats a wrong id",status_code=status.HTTP_404_NOT_FOUND)
    db.delete(task_obj)
    db.commit()
    return{
        "Message":"Task deleted successfully."
    }