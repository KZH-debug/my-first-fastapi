from fastapi import FastAPI, Response

app = FastAPI()

# 1. Fix the 404 Favicon icon request
@app.get("/favicon.ico")
def disable_favicon():
    return Response(status_code=204)

# 2. Your main homepage pathway (/)
@app.get("/")
def home():
    return {
        "message": "Mingalaba! Welcome to the Homepage!",
        "status": "Online",
        "page": "Home"
    }

# 3. BRAND NEW PATHWAY: Your About Page (/about)
@app.get("/about")
def about_page():
    return {
        "developer": "A student learning Python backend",
        "city": "Yangon, Myanmar",
        "goal": "To become a Machine Learning Engineer",
        "tools_used": ["Termux", "FastAPI", "Python"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

