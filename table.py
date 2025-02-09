import google.generativeai as genai
import numpy as np
from dotenv import load_dotenv
import sqlite3

load_dotenv()

import os
key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=key)

model = genai.GenerativeModel("gemini-1.5-flash")
prompt=[""" you are an expert in converting natural Question to SQL Query,
        The SQL database employee.db has the table name emptab and has the following columns - empid,empname,empsalary
        \n\n For Example \n Example 1- For selecting all the columns from the table! the sql query will be something like
        select * from emptab; \n Example-2 For selecting the name of the employee who got salary more than 10000 ! the 
        sql query will be something like select empname from emptab where salary>1000; also the sql query should not
        have ''' in the beginning or end of sql and elimitate the word sql in the output """]

question="select names of the employee with salary whose empsalary is greater than 3500"

def get_gemini_response(quest,prompt):
    model=genai.GenerativeModel("gemini-1.5-flash")
    res=model.generate_content([prompt[0],quest])
    print(res.text)

response=get_gemini_response(quest = question,prompt=prompt[0])

def hit_sqldatabase(query,db):
    connection=sqlite3.connect(db)
    cursor=connection.cursor()
    data=cursor.execute(query)
    for i in data:
        print(i)
    connection.commit()
    connection.close()
    
    
hit_sqldatabase(response,"employee.db")