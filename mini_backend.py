from fastapi import FastAPI
app = FastAPI()
@app.get("/")

def main_page():
	return {"message": "My first backend project is working!"}

@app.get("/hello/{name}")
def personal_greet(name: str):
	return {"message": f"Hello {name}!"}
