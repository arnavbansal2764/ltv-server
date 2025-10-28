from fastapi import FastAPI
import random

app = FastAPI()


@app.post("/")
def score():
	"""Return a random float score for the provided contact."""
	return {"score": random.random()}

@app.get("/")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}


if __name__ == "__main__":
	# Simple local runner for development: python main.py
	import uvicorn

	uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

