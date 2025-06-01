# Image analyzer Web application
Enter any image URL in the format of ".jpg" or ".jpeg" to get an AI-generated description and detect objects within the image using YOLO. The app also shows image metadata like size and dimensions, and displays the image with bounding boxes highlighting detected objects.

# Project Structure
You have to make 3 separate folders in the root project folder, name "app", "templates", "static"
In the app folder you have to add the following files that i have shared above:
1. caption_generator.py
2. main.py
3. utils.py
4. yolo_detector.py
For the templates folder add only the "index.html" file 
For the static folder add only the "style.css" file

# How to Run
1. Create and activate a virtual environment.
2. Install dependencies from requirements.txt.
3. Run the app with:
   uvicorn app.main:app --reload
4. Open your browser at http://localhost:8000 and enter an image URL to analyze.

# Output
The look of website is uploaded by the name as "output 1" and "output 2"
