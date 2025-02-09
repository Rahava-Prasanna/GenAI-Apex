import numpy as np
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

import os
key=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key = key)

model=genai.GenerativeModel("gemini-1.5-flash")

print(model)

res = model.generate_content("Who is the CEO of Google")

print(res.text)