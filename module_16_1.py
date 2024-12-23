from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def user_admin():
    return {"message": "Вы вошли как администаратор"}

@app.get("/user/{user_id}")
async def user_id(id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

