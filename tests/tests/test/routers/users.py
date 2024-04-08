from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "lxw"}, {"username": "xinet"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "lxw"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
