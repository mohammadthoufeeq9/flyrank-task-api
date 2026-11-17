from pydantic import BaseModel

class Taskcreate(BaseModel):
    title:str


class TaskUpdate(BaseModel):
    title:str|None=None
    done:bool|None=None