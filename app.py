import streamlit as st
import tensorflow as tf
import numpy as np
from streamlit_drawable_canvas import st_canvas
from PIL import Image, ImageOps

# Load trained CNN model
model = tf.keras.models.load_model("mnist_cnn.keras")

# Page settings
st.set_page_config(
    page_title="Handwritten Digit Recognition",
    page_icon="🔢"
)

st.title("🔢 Handwritten Digit Recognition")
st.write("Draw a digit from 0 to 9 using your mouse.")

# Drawing canvas
canvas_result = st_canvas(
    fill_color="black",
    stroke_width=15,
    stroke_color="white",
    background_color="black",
    width=280,
    height=280,
    drawing_mode="freedraw",
    key="canvas"
)

# Predict button
if st.button("Predict"):

    if canvas_result.image_data is not None:

        # Get canvas image
        image = canvas_result.image_data

        # Convert RGBA to grayscale
        image = Image.fromarray(image.astype("uint8")).convert("L")

        # Resize to MNIST size
        image = image.resize((28, 28))

        # Convert to numpy array
        image_array = np.array(image)

        # Normalize
        image_array = image_array.astype("float32") / 255.0

        # Add channel and batch dimensions
        image_array = image_array.reshape(1, 28, 28, 1)

        # Prediction
        prediction = model.predict(image_array, verbose=0)

        predicted_digit = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        # Display result
        st.success(f"Predicted Digit: {predicted_digit}")
        st.info(f"Confidence: {confidence:.2f}%")