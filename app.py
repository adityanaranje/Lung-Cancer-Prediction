import numpy as np
import streamlit as st
import pickle
import time
import base64

bg = "static/bg2.jpg"
bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{bg_ext};base64,{base64.b64encode(open(bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Lung Cancer Prediction")
st.subheader("Enter Details")

arr = []

col1, col2 = st.columns(2)
with col1:
    x = st.selectbox('Gender',['Male','Female'])
    if x=='Male':
        arr.append(1)
    else:
        arr.append(0)

with col2:
    x = st.number_input('Age',0,100,1)
    arr.append(x)

col1, col2, col3 = st.columns(3)
with col1:
    x = st.selectbox('Smoking',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)
with col2:
    x = st.selectbox('Yellow Fingers',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)
with col3:
    x = st.selectbox('Anxiety',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)


col1, col2, col3 = st.columns(3)
with col1:
    x = st.selectbox('Peer Pressure',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)
with col2:
    x = st.selectbox('Chronic Disease',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)
with col3:
    x = st.selectbox('Fatigue',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)


col1, col2, col3 = st.columns(3)
with col1:
    x = st.selectbox('Allergy',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)
with col2:
    x = st.selectbox('Weezing',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)
with col3:
    x = st.selectbox('Alcohol Consumption',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)


col1, col2, col3, col4 = st.columns(4)
with col1:
    x = st.selectbox('Coughing',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)
with col2:
    x = st.selectbox('Shortness Of Breath',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)
with col3:
    x = st.selectbox('Swallowing Difficulty',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)
with col4:
    x = st.selectbox('Chest Pain',['Yes','No'])
    if x=='Yes':
        arr.append(1)
    else:
        arr.append(0)



if st.button('Predict'):
    lst = np.array(arr).reshape(1, 15)
    loaded_model = pickle.load(open("model/lung_cancer.pkl", "rb"))
    result = loaded_model.predict(lst)

    with st.spinner("Predicting.....Have Patience"):
        time.sleep(2)
    if result==1:
        st.error("Chance Of Disease")
    if result==0:
        st.success("No Chance Of Disease")
