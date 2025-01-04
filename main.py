from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
async def submit(
    request: Request,
    team_name: str = Form(...),
    code: str = Form(None),
    code_file: UploadFile = File(None)
):
    if code_file:
        code_content = await code_file.read()
        code = code_content.decode('utf-8')
    elif not code:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "message": "Molimo vas da unesete kod ili otpremite fajl"
        })

    # Here you can add logic to handle the submission
    return templates.TemplateResponse("index.html", {
        "request": request,
        "message": f"Primljena prijava od tima: {team_name}"
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
