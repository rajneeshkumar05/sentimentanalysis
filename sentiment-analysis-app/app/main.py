from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from app.model import analyze_sentiment

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(request: Request):
    form = await request.form()
    text = form["text"]
    result = analyze_sentiment(text)
    return result
