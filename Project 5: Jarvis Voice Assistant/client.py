from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
 
# pip install openai 
# Set your OpenAI API key as an environment variable:
# export OPENAI_API_KEY="your-api-key-here"
# Or create a .env file with: OPENAI_API_KEY=your-api-key-here

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY", "<Your OpenAI API Key Here>")
)

try:
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "you are a virtual assistent, name jarvis skilled in general tasks like Alexa and Google Cloud"},

        {"role": "user", "content": "What is coding"}
      ]
    )
    print("API Response:")
    print(completion.choices[0].message)

except Exception as e:
    print(f"API Error: {e}")
    print("\n--- Mock Response for Testing ---")
    print("Coding is the process of creating computer programs by writing instructions in programming languages. It involves problem-solving, logic, and creativity to build software that can perform specific tasks. Programmers use languages like Python, JavaScript, Java, and many others to communicate with computers and create applications, websites, games, and other digital solutions.")
    print("\nNote: This is a mock response because the OpenAI API quota has been exceeded.")
    print("To use the real API, please check your OpenAI account billing and quota limits.")
