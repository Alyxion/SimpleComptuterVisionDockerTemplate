import streamlit as st
import pandas as pd
import numpy as np
import cv2
import time
import requests


# Uploader widget
st.sidebar.title("Upload Your File")
filename = st.sidebar.file_uploader("Choose an image file", type=['jpg', 'png'])
st.sidebar.markdown("---")

st.title("Just a demo server")
st.header("Some header")
st.write("First quarter")
q1_sales = {
    "January": 100,
    "February": 200,
    "March": 300
}
st.write(q1_sales)

st.write("Second quarter")
q2_sales = {
    "April": 300,
    "May": 400,
    "June": 500
}
st.write(q2_sales)

q2_df = pd.DataFrame(q2_sales.items(), columns=["Month", "Amount"])
st.dataframe(q2_df)
st.line_chart(q2_df)

target = None

try:
    version = requests.get("http://yourwebservice:5000/version").text
    st.write(f"Using classifier version {version}")
except:
    st.write("Could not connect to classification service")


@st.cache
def try_read_image(file_data):
    image = cv2.imdecode(np.frombuffer(file_data, dtype=np.uint8), cv2.IMREAD_ANYCOLOR)
    return image


if filename:  # fetch image and animate it once uploaded
    image = try_read_image(filename.getvalue())

    # Now testing the web service. In practice you could for example call your real inference within it:
    response = requests.post("http://yourwebservice:5000/inference/classify", data=filename.getvalue())
    st.write(response.text)

    last_image = None
    for counter in range(10):
        time.sleep(0.1)
        if last_image is not None:
            image = (image * 0.90).astype(np.uint8)
            last_image.image(image)
        else:
            last_image = st.image(image)
