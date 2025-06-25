from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Initialize FastAPI app
app = FastAPI()

# Load Tokenizer
with open("tokenizer.pkl", "rb") as handle:
    tokenizer = pickle.load(handle)
print("✅ Tokenizer loaded.")

# Load Model
model = tf.keras.models.load_model("word_classifier.h5")
print("✅ Model loaded.")

# Define Pydantic model for JSON request
class TextInput(BaseModel):
    text: str

# Harassment categories
categories = {0: "Low", 1: "Medium", 2: "High"}

@app.post("/classify")
def classify_text(input_data: TextInput):
    """Classifies text as low, medium, or high harassment."""
    if not input_data.text:
        return {"error": "Text cannot be empty"}
    
    sequence = tokenizer.texts_to_sequences([input_data.text])
    padded_sequence = pad_sequences(sequence, maxlen=5)  # Ensure same padding
    prediction = model.predict(padded_sequence)
    label = np.argmax(prediction)

    return {"text": input_data.text, "category": categories[label], "confidence": prediction.tolist()}
