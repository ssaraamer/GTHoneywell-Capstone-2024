from http.client import HTTPException
from fastapi import FastAPI, Depends, File, UploadFile
from config import settings
from db.session import SessionLocal, engine
from db.base_class import Base
from sqlalchemy.orm import Session
from crud import create_query, update_query_response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from lllama_development import get_llama_response
from schemas import QueryCreate, QueryResponse
from fastapi.responses import JSONResponse
import fitz

Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    return app


app = start_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

class QueryIn(BaseModel):
    query: str

class QueryOut(BaseModel):
    id: int
    query: str
    response: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Takes text query from user and hands it to LLM
@app.post("/query/", response_model=QueryOut)
def get_chat_response(query_in: QueryIn):
    """
    Accepts a user query and returns a response from the LLM.
    """
    try:
        response_text = get_llama_response(query_in.query)
        print(response_text)
        return QueryOut(id=0, query=query_in.query, response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#stores created query
@app.post("/query/", response_model=QueryResponse)
def store_created_query(query_in: QueryCreate, db: Session = Depends(get_db)):
    db_query = create_query(db, query_text=query_in.query)
    llama_response = get_llama_response(query_in.query)
    updated_query = update_query_response(db, db_query.id, llama_response)
    return updated_query

@app.get("/")
def home():
    return {"msg": "Welcome to the Honeywell chatbot FastAPI server. To visit the FastAPI UI go to http://localhost:8000/docs#/"}

#Handles PDF upload to LLM by converting PDF to text and then passing the text to the LLM
@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        return JSONResponse(content={"message": "Invalid file type"}, status_code=400)

    try:
        contents = await file.read()
        extracted_text = extract_text_from_pdf(contents)
        llama_response = get_llama_response(extracted_text)
        print(llama_response)
        #Able to nswers questions after this message displayed
        return {"llm_response": llama_response, "message": "File uploaded successfully"}
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)

def extract_text_from_pdf(contents):
    text = ''
    doc = fitz.open(stream=contents, filetype="pdf")
    for page in doc:
        text += page.get_text("text")
    return text