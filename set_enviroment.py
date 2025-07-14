import os
import google.generativeai as genai

google_api_key = os.environ.get("GOOGLE_API_KEY")
tavily_api_key = os.environ.get("TAVILY_API_KEY")
genai.configure(api_key=google_api_key)

os.environ["GOOGLE_API_KEY"] = google_api_key
os.environ["TAVILY_API_KEY"] = tavily_api_key