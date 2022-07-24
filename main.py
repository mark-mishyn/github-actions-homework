from fastapi import FastAPI

app = FastAPI()


@app.get("/sum/{a}/{b}")
def root(a, b):
    try:
        return {"sum": float(a) + float(b)}
    except ValueError:
        return {"error": "valid numbers are required"}
