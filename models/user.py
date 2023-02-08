from pydantic import BaseModel,EmailStr


class User(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    UUID:int

class Candidate(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    UUID:int
    career_level:str
    job_major:str
    year_of_experience:float
    degree_type:str
    skill:str
    nationality:str
    city:str
    salary:str
    gender:str
