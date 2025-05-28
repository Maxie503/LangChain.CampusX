from pydantic import BaseModel
from typing import Optional

class studentclass(BaseModel):
    name: str = 'Dnitesh'
    age: int
    sname : Optional[str] = None
    

nstudent = {'name': "nitesh",'age': '32'}

student = studentclass(**nstudent)


print(student)