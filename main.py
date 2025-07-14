"""FastAPI webapp."""
import logging
import set_enviroment # loading api keys
from langchain_google_genai import ChatGoogleGenerativeAI   
from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from langchain_core.messages import HumanMessage
import uvicorn
from image_message import image_message # function to wrap llm input with image
from initialize_cooking_agent import cooking_agent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# from config import set_environment
# set_environment()

# Initialize FastAPI app
app = FastAPI()

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize a non-streaming LLM for the regular API endpoints
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 0)
# Root endpoint
@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.get("/test")
# async def test():
#     return {"message": "This is a test endpoint."}

# Chat endpoint
@app.post("/chat")
async def chat(
    message: str = Form(...), 
    image: UploadFile = File(None)
):
    # process image and text message
    if image:
        contents = await image.read()
        # Placeholder logic for image usage:
        if not message.strip():
            message = "Give a short description of the image."
        response = cooking_agent(llm).invoke({"messages" : image_message(message, contents)})
        response = response['messages'][-1]
         # default message if none provided
        return {"response": response.content}

    # Process text message
    messages = [HumanMessage(content=message)]
    response = llm.invoke(messages)
    
    return {"response": response.content}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

