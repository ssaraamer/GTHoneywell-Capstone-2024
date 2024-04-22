from sqlalchemy.orm import Session
from models import Query

def create_query(db: Session, query_text: str):
    db_query = Query(query_text=query_text)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query

#This function updates the query response with the response
def update_query_response(db: Session, query_id: int, response: str):
    db_query = db.query(Query).filter(Query.id == query_id).first()
    db_query.response = response
    db.commit()
    return db_query