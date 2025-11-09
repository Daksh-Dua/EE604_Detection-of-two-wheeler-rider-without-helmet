from FinalDemo import process_image
import streamlit as st
import numpy as np
import cv2

st.title("🪖 Helmet and Plate Detection")
uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png","webp","avif"])
if uploaded:
    img = cv2.imdecode(np.frombuffer(uploaded.read(), np.uint8), 1)
    st.image(img, caption="Original", channels="BGR")
    annotated, ocr_results = process_image(img)
    st.image(annotated, caption="Detections", channels="BGR")

    if ocr_results:
      st.subheader("Detected License Plate Texts")
      for i, item in enumerate(ocr_results, 1):
        st.write(f"**Plate {i}:** {item['text']}")
    else:
      st.info("No readable license plates found.")

