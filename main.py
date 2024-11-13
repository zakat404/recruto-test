import os
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
async def greet(name: Optional[str] = "Recruto", message: Optional[str] = "Давай дружить"):
    return {"message": f"Hello {name}! {message}!"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
