from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
async def greet(name: Optional[str] = "Recruto", message: Optional[str] = "Давай дружить"):
    return {"message": f"Hello {name}! {message}!"}
