
from fastapi import FastAPI

app = FastAPI() 

fake_db = [
    {
        "id": 0,
        "username": "john_doe",
    },
    {
        "id": 1,
        "username": "jane_smith",
    },
]

@app.get("/get_user")
def get_user(user_id: int):
    for user in fake_db:
        if user["id"] == user_id:
            return fake_db[user_id]
    return {"error": "User not found"}

@app.post("/post_user")
def post_user(username: str):
    new_user = {
        "id": len(fake_db),
        "username": username,
    }
    fake_db.append(new_user)
    return new_user

@app.put("/update_user")
def update_user(user_id: int, username: str):
    for user in fake_db:
        if user["id"] == user_id:
            user["username"] = username
            return fake_db[user_id]
    return {"error": "User not found"}

@app.delete("/delete_user")
def delete_user(user_id: int):
    del fake_db[user_id]
    return {"message": "User deleted successfully"}