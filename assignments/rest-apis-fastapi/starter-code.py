from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TODO: Add your routes and models here
# Hint: Use @app.get() and @app.post() decorators to define endpoints
# Use Pydantic models to define request/response data structures

# Example model (uncomment and modify as needed):
# class Item(BaseModel):
#     name: str
#     price: float
#     description: str = None


# Start with a simple GET endpoint to test if your setup works
# Then add more complex routes with path and query parameters
