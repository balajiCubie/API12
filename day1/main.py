from fastapi import FastAPI
import random
import string

app = FastAPI()

@app.get("/")
async def generate_password(length: int = 12):
    """
    Generate a random password of the given length.
    """
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    return {"password": password}
