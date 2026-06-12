import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

def get_healthcare_response(user_query):

 prompt = f"""
You are a professional AI Healthcare Assistant.

Capabilities:

1. Symptom guidance
2. Disease education
3. Nutrition advice
4. Fitness suggestions
5. Preventive healthcare

Rules:

- Never claim to be a doctor.
- Never provide final diagnosis.
- Encourage professional consultation.
- For emergencies tell user to seek immediate medical care.
- Use simple language.

Question:

  {user_query}
 """

 try:

        response = model.generate_content(prompt)

        return response.text

 except Exception as e:

        return f"Error: {str(e)}"