# -*- coding: utf-8 -*-
"""
KrishiMitra AI - Plant Disease Inference Engine
Preprocesses leaf images to exact input specifications (224x224 RGB, [0, 1] normalization)
Runs inference using the real trained Keras model: models/plant_disease_model.keras
Maps predictions to the exact training class array and queries the verified knowledge base.
"""

import os
import numpy as np
from PIL import Image
import keras
from disease_knowledge_base import CLASS_NAME_LIST, get_disease_info

_MODEL_INSTANCE = None

def get_disease_model(model_path=None):
    """Singleton cached loader for the real trained Keras model."""
    global _MODEL_INSTANCE
    if _MODEL_INSTANCE is None:
        if not model_path:
            base_dir = os.path.abspath(os.path.dirname(__file__))
            model_path = os.path.join(base_dir, "models", "plant_disease_model.keras")
            
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Trained model not found at: {model_path}")
            
        print(f"Loading trained plant disease model from: {model_path}")
        _MODEL_INSTANCE = keras.models.load_model(model_path)
        print("Model loaded successfully into memory.")
        
    return _MODEL_INSTANCE


def predict_disease(image_path, lang="mr", model_path=None):
    """
    Validates, preprocesses, and classifies a crop leaf image.
    Returns prediction score, condition classification, and dual treatment plans.
    """
    if not os.path.exists(image_path):
        return {"error": "Image file not found on disk."}

    try:
        # 1. Image preprocessing with Pillow
        with Image.open(image_path) as img:
            # Ensure RGB format (handles RGBA, grayscale, CMYK)
            if img.mode != "RGB":
                img = img.convert("RGB")
            
            # Exact dimensions required by CNN model
            img = img.resize((224, 224), Image.Resampling.LANCZOS)
            img_array = np.asarray(img, dtype=np.float32)

        # 2. Normalization & Batch dimension
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # 3. Model Inference
        model = get_disease_model(model_path)
        prediction = model.predict(img_array, verbose=0)
        
        predicted_index = int(np.argmax(prediction[0]))
        confidence = float(np.max(prediction[0]) * 100.0)

        # 4. Class Mapping
        if 0 <= predicted_index < len(CLASS_NAME_LIST):
            class_name = CLASS_NAME_LIST[predicted_index]
        else:
            class_name = "Unknown"

        # 5. Retrieve Knowledge Base & Treatment Plans
        disease_info = get_disease_info(class_name, lang=lang)

        # Determine reliability warning
        low_confidence = confidence < 50.0

        return {
            "success": True,
            "predicted_index": predicted_index,
            "class_name": class_name,
            "confidence": round(confidence, 2),
            "low_confidence": low_confidence,
            "disease_info": disease_info,
            "probabilities": {
                CLASS_NAME_LIST[i]: round(float(prediction[0][i]) * 100.0, 2)
                for i in range(len(CLASS_NAME_LIST))
            }
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Error running inference pipeline: {str(e)}"
        }
