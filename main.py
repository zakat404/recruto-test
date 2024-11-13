from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root(name: str = "Recruto", message: str = "Давай дружить!"):
    return f"Hello {name}! {message}"
