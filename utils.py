import requests
from PIL import Image
import io

def fetch_image(url: str) -> Image.Image:
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Failed to fetch image from URL.")
    return Image.open(io.BytesIO(response.content)).convert("RGB")