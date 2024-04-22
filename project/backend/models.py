from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class using the declarative base provided by SQLAlchemy.
# This base class will be used to declare concrete classes that represent database tables.
Base = declarative_base()

class Query(Base):
    """
    Represents a 'queries' table in the database using SQLAlchemy ORM.
    
    Attributes:
        id (Column): An integer column that represents the primary key, automatically indexed.
        query_text (Column): A string column to store the query text, indexed to enhance search performance.
        response (Column): A string column to store the response associated with the query text, also indexed.
    """
    # Name of the table in the database
    __tablename__ = 'queries'

    # Defining columns in the database table
    id = Column(Integer, primary_key=True, index=True)  # Primary key column, automatically indexed by SQLAlchemy
    query_text = Column(String, index=True)  # Text of the query, indexed for quicker searches
    response = Column(String, index=True)  # Text of the response associated with the query, indexed for performance