from fastapi import FastAPI
from typing import Optional
from database import query_db, query_db_dynamic

app= FastAPI()

@app.get('/alloggi')
def ricerca_alloggi(year, comune):
    return query_db(year, comune)

@app.get('/alloggi_dynamic')
def ricerca_alloggi_dyn(year:Optional[int]=None, comune:Optional[str]=None):
    return query_db_dynamic(year, comune)
