from pydantic import BaseModel

# Schema for incoming query data
class QueryCreate(BaseModel):
    query: str

# Schema for outgoing data, including the response from the Llama API
class QueryResponse(BaseModel):
    id: int
    query: str
    response: str

    class Config:
        orm_mode = True