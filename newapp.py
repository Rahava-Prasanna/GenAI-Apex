import google.generativeai as genai
from dotenv import load_dotenv
import sqlite3
import os
load_dotenv()

import os
key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=key)

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel("gemini-pro")
    res=model.generate_content([prompt[0],question])
    return res.text

def hit_sql_database(query,db):
    connection=sqlite3.connect(db)
    cursor=connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    
    
    connection.commit()
    connection.close()
    for row in rows:
        print(row)
    return rows

    


prompt=["""
                   You are an expert in converting English question to SQL Query!
                   The SQL database Students has the name Students and has the following columns-
                   NAME,CLASS,SECTION,MARK \n\n For Example ,\n Example-1- How many entries
                   of records are present?, the SQL command will be something like this
                   SELECT COUNT(*) FROM Students;\n Example-2-Tell me all the students belongs to Data science?,
                   the SQL command will be something like this SELECT * FROM STUDENTS where CLASS=='Data science'; 
                   also the sql code should not have ``` in beginning or end and sql word in the output"""]

question = "What is the maximum marks in the Students table?"

res = get_gemini_response(prompt=prompt,question=question)
print(res)
hit_sql_database(res,"Students.db")