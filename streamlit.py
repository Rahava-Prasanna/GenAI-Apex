from urllib import response
import google.generativeai as genai
from dotenv import load_dotenv
import sqlite3
import os
import streamlit as st

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = ["""
You are an expert in converting English questions to SQL queries! 
The SQL database 'Students' has the following columns: NAME, CLASS, SECTION, MARK.

Examples:
Example 1: "How many entries of records are present?" 
SQL Command: SELECT COUNT(*) FROM Students;

Example 2: "Tell me all the students who belong to Data Science?" 
SQL Command: SELECT * FROM Students WHERE CLASS = 'Data Science';

Ensure the SQL code does not have backticks (`) or the word 'sql' in the output.
"""]

def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        res = model.generate_content([prompt[0], question])
        print(f"Generated Response: {res.text}")  # Debugging
        return res.text.strip()
    except Exception as e:
        print(f"Error generating SQL query: {e}")
        return None

def hit_sqldatabase(query, db):
    print(f"Executing SQL Query: {query}") 
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.close()
    return rows

# Streamlit App
st.set_page_config(page_title="SQL Query Generator", layout="wide")
st.header("Gemini SQL Query Generator")

question = st.text_input("Enter your question about the Students database:")
submit = st.button("Generate SQL Query and Fetch Data")

if submit:
    if question.strip():
        sql_query = get_gemini_response(question, prompt)
        if sql_query:
            st.subheader("Generated SQL Query:")
            st.code(sql_query, language="sql")
            results = hit_sqldatabase(sql_query, "Students.db")
            st.subheader("Query Results:")
            if results and isinstance(results[0], tuple):
                for row in results:
                    st.write(row)
            else:
                st.error(results[0] if results else "No results found.")
        else:
            st.error("Failed to generate a valid SQL query.")
    else:
        st.error("Please enter a question.")