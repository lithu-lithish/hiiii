from fastapi import FastAPI, Path
app = FastAPI()
@app.get("/")
def firstapi():
    return {"message":"Hello world"}
