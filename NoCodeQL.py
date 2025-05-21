import os
from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore
from pinecone import Pinecone
import nest_asyncio
import uvicorn
from threading import Thread

# Set up API and index name
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "pcsk_685TYA_7fL6c5qXeMqsatFLhLRBqmg1K5neZ1vKoNf5S1grpQM5UfGQjgFCLRfu4cZXGYq")
INDEX_NAME = os.getenv("PINECONE_INDEX", "nocodeql")

# Initialize Pinecone client (no init(), no environment)
pc = Pinecone(api_key= "pcsk_685TYA_7fL6c5qXeMqsatFLhLRBqmg1K5neZ1vKoNf5S1grpQM5UfGQjgFCLRfu4cZXGYq")
index = pc.Index("nocodeql")

# Define FastAPI app
app = FastAPI()

class QueryRequest(BaseModel):
    vector: list

@app.post("/search")
def search(req: QueryRequest):
    result = index.query(vector=req.vector, top_k=5, include_metadata=True)
    return {"matches": result.get("matches", [])}

