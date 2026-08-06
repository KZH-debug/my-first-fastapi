import os
import uvicorn
from fastapi import FastAPI, Response, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Kyaw Zaw Han | Engineering Portal")

# Link FastAPI to your templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/favicon.ico")
def disable_favicon():
    return Response(status_code=204)

# 1. Main Homepage Pathway (/)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "home.html", 
        {
            "request": request,
            "title": "KZH | Software Engineer",
            "name": "Kyaw Zaw Han",
            "role": "Python Backend & Software Engineer"
        }
    )

# 2. About Page Pathway (/about)
@app.get("/about", response_class=HTMLResponse)
def about_page(request: Request):
    return templates.TemplateResponse(
        "about.html", 
        {
            "request": request,
            "title": "About Kyaw Zaw Han",
            "name": "Kyaw Zaw Han (KZH)",
            "education": "B.A. Degree in Psychology",
            "specialization": "Python Web Backend & Software Engineering",
            "city": "Yangon, Myanmar",
            "goal": "Machine Learning Engineer",
            "tools": ["Termux", "FastAPI", "Python", "Tailwind CSS", "Git / GitHub", "Render Cloud"]
        }
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

