from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.utils import fetch_image
from app.yolo_detector import detect_objects
from app.caption_generator import generate_caption
from PIL import Image
import uvicorn
import os
from uuid import uuid4

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, image_url: str = Form(...)):
    try:
        image: Image.Image = fetch_image(image_url)
        caption = generate_caption(image)
        detections, drawn_image = detect_objects(image)

        metadata = {
            "format": image.format or "N/A",
            "mode": image.mode or "N/A",
            "width": image.width,
            "height": image.height,
            "size_kb": None  # optional: implement if needed
        }

        # Save image with detections in static folder with a unique name
        output_filename = f"output_{uuid4().hex[:8]}.jpg"
        output_path = os.path.join("static", output_filename)
        drawn_image.save(output_path)

        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": {
                "description": caption,
                "objects": detections,
                "image_url": image_url,
                "output_image": f"/static/{output_filename}",
                "metadata": metadata
            }
        })
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": str(e),
            "result": None
        })

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
