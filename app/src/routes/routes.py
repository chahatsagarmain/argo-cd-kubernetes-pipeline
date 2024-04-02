from fastapi import APIRouter , HTTPException
from controllers.controllers import user_controller

router = APIRouter()

@router.get("/users")
async def get_users():

    query_set = await user_controller()
    
    return query_set

@router.get("/users/{user_id}")
async def get_user(user_id : int | None):
    
    if user_id is None:
        return HTTPException(401 , { "message" : "query string missing"})
    
    query_set = await user_controller()
    
    if user_id in query_set:
        return {"message" : "User present" , "user" : query_set[user_id]}
    
    return HTTPException(404 , {"message" : "user with user id not present"})

@router.get("/new")
async def new_route():
    
    return {"message" : "this is new route your on 0.2.0"}