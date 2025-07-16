import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ✅ Must be the first Streamlit command
st.set_page_config(page_title="CIFAR‑10 Demo", page_icon="🚀")

# CIFAR-10 class names
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Load the trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('cifar10_model.h5')  # update if named differently
    return model

model = load_model()

# Page title
st.title("🚀 CIFAR-10 Image Classifier")
st.write("Upload a 32x32 image of an object (airplane, cat, dog, etc.) and I'll tell you what it is!")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Display image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    image_resized = image.resize((32, 32))
    img_array = np.array(image_resized) / 255.0
    img_batch = np.expand_dims(img_array, axis=0)

    # Predict
    preds = model.predict(img_batch)
    pred_class = np.argmax(preds)
    confidence = np.max(preds)

    st.markdown("### 🎯 Prediction:")
    st.success(f"**{class_names[pred_class]}** with **{confidence:.2%}** confidence")

    # Optional: show probabilities
    if st.checkbox("Show class probabilities"):
        for i, p in enumerate(preds[0]):
            st.write(f"{class_names[i]:>10}: {p:.2%}")
