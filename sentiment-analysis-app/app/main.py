from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.model import analyze_sentiment

app = FastAPI()

# Templates directory setup
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    # Home page (index.html) ko render kar raha hai
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):
    form = await request.form()
    text = form.get("text", "")
    
    # Model se sentiment analysis le rahe hain
    # Maan lijiye result format ye hai: {"label": "Positive", "score": 0.98}
    result = analyze_sentiment(text)
    
    # Agar analyze_sentiment sirf string deta hai (e.g. "Positive"), 
    # toh niche wala code data ko handle kar lega:
    sentiment_label = result.get("label", result) if isinstance(result, dict) else result
    confidence_score = result.get("score", 0.95) if isinstance(result, dict) else 0.95

    # Result page (result.html) par data bhej rahe hain
    return templates.TemplateResponse("result.html", {
        "request": request,
        "sentiment": sentiment_label,
        "score": round(confidence_score * 100, 1), # 95.5 ki tarah dikhega
        "original_text": text
    })
