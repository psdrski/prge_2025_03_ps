from fastapi import APIRouter

router = APIRouter()

@router.get("/users_static")
async def get_user():
    return [{"id":123132131321, "name":"Mikołaj", "location":"Kielce", "posts": 12},
            {"id": 123132131321, "name": "Piotr", "location": "Garwolin", "posts": 32},
            {"id": 123132131321, "name": "Rafal", "location": "Turek", "posts": 42},
            {"id": 123132131321, "name": "Adam", "location": "Szczecin", "posts": 22},
            {"id": 123132131321, "name": "Ola", "location": "Bialystok", "posts": 11},]

