from fastapi import FastAPI, UploadFile, File
from predictor import predict_image
from PIL import Image
import io

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    pred_class = predict_image(image)
    return {"predicted_class": pred_class}
