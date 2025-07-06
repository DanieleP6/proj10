import os
import sqlite3
from typing import Optional

cur_dir= os.getcwd()
db_dir = os.path.join(cur_dir, 'database') # creazione del path per il database
db_path = os.path.join(db_dir, 'veneto_case.db') # creazione del path per il database

def query_db(year,comune):
    query= f"SELECT * FROM veneto_case WHERE Anno = {year} AND Comune = '{comune}'"
    conn = sqlite3.connect(db_path) # connessione al database
    cursor= conn.cursor() # creazione del cursore
    cursor.execute(query) # esecuzione della query
    results = cursor.fetchall() # recupero dei risultati
    conn.close()  # chiusura della connessione al database
    return results #ritornare sempre i risultati

def query_db_dynamic(year:Optional[int], comune:Optional[str]):
    query = "SELECT * FROM veneto_case WHERE 1=1"
    if year is not None:
        query += f" AND Anno = {year}"
    if comune is not None:
        query += f" AND Comune = '{comune}'"
    print(query)
    conn = sqlite3.connect(db_path)  # connessione al database
    cursor = conn.cursor()  # creazione del cursore
    cursor.execute(query)  # esecuzione della query
    results = cursor.fetchall()  # recupero dei risultati
    conn.close()  # chiusura della connessione al database
    return results  # ritorna i risultati della query

