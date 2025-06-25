from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for all origins (adjust for security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Tokenizer
try:
    with open("tokenizer.pkl", "rb") as handle:
        tokenizer = pickle.load(handle)
    print("✅ Tokenizer loaded.")
except Exception as e:
    print(f"❌ Error loading tokenizer: {e}")
    tokenizer = None

# Load Model
try:
    model = tf.keras.models.load_model("word_classifier.h5")
    print(f"✅ Model loaded. Expected input shape: {model.input_shape}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# Define Pydantic model for JSON request
class TextInput(BaseModel):
    text: str

# Harassment categories
categories = {0: "Low", 1: "Medium", 2: "High"}

# **Ensure MAX_LEN matches training data**
MAX_LEN = model.input_shape[1] if model else 20  # Use the actual expected shape

@app.post("/classify")
def classify_text(input_data: TextInput):
    """Classifies text as low, medium, or high harassment."""
    if not input_data.text.strip():
        return {"error": "Text cannot be empty"}

    if tokenizer is None or model is None:
        return {"error": "Model or tokenizer not loaded"}

    # Tokenization and padding
    sequence = tokenizer.texts_to_sequences([input_data.text])
    print(f"🔍 Tokenized sequence: {sequence}")  # Debugging output

    padded_sequence = pad_sequences(sequence, maxlen=MAX_LEN)
    print(f"📏 Padded input shape: {padded_sequence.shape}")  # Debugging output

    # Ensure shape matches model expectations
    expected_shape = (1, MAX_LEN)  # Batch size of 1
    if padded_sequence.shape != expected_shape:
        return {"error": f"Shape mismatch! Expected {expected_shape}, got {padded_sequence.shape}"}

    # Predict category
    prediction = model.predict(padded_sequence)
    print(f"📊 Prediction output: {prediction}")  # Debugging output

    label = np.argmax(prediction)

    return {
        "text": input_data.text,
        "category": categories[label],
        "confidence": prediction.tolist()
    }

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "OK", "model_loaded": model is not None, "tokenizer_loaded": tokenizer is not None}

