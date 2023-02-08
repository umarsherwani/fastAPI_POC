def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "first_name": item["first_name"],
        "last_name": item["last_name"],
        "email": item["email"],
        "UUID": item["UUID"],
        "career_level": item["career_level"],
        "job_major":item["job_major"],
        "year_of_experience":item["year_of_experience"],
        "degree_type":item["degree_type"],
        "skill":item["skill"],
        "nationality":item["nationality"],
        "city":item["city"],
        "salary":item["salary"],
        "gender":item["gender"]
    }


# def userEntity(item) -> dict:
#     return {
#         "id":str(item["_id"]),
#         "name":item["name"],
#         "email":item["email"],
#         "password":item["password"]
#     }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]

