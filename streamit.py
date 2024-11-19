# -*- coding: utf-8 -*-
"""streamit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TQr6C4yvw9eAQ6uqWPPGYyt2YJcoOKPj
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# ฟังก์ชันสำหรับโหลดข้อมูล
@st.cache
def load_data(file):
    df = pd.read_csv(file)
    return df

# ฟังก์ชันสำหรับ Train โมเดล
def train_model(df):
    X = df[['R', 'G', 'B']] / 255.0  # Normalize RGB
    y = df['season']

    # แปลง Labels เป็นตัวเลข
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # แบ่งข้อมูล Train, Test
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

    # ปรับขนาดข้อมูล
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # สร้างโมเดล SVM และ Train
    svm_model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
    svm_model.fit(X_train, y_train)

    return svm_model, scaler, label_encoder

# ส่วน UI หลักของ Streamlit
def main():
    st.title("Color to Season Classifier")
    st.write("Train the model using a dataset and then predict the season for a specific RGB color.")

    # อัปโหลดไฟล์ CSV
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        # โหลดข้อมูล
        df = load_data(uploaded_file)
        st.write("Dataset Preview:")
        st.dataframe(df.head())

        # ตรวจสอบคอลัมน์ที่ต้องการ
        required_columns = {'R', 'G', 'B', 'season'}
        if not required_columns.issubset(df.columns):
            st.error(f"The uploaded file must contain the following columns: {', '.join(required_columns)}")
            return

        if st.button("Train Model"):
            st.write("Training the model...")
            svm_model, scaler, label_encoder = train_model(df)
            st.success("Model training completed!")

            # รับค่า RGB จากผู้ใช้
            st.write("Enter RGB values to predict the season:")
            r = st.number_input("Red (R)", min_value=0, max_value=255, value=128)
            g = st.number_input("Green (G)", min_value=0, max_value=255, value=128)
            b = st.number_input("Blue (B)", min_value=0, max_value=255, value=128)

            if st.button("Predict Season"):
                # เตรียมข้อมูล RGB สำหรับพยากรณ์
                rgb_input = np.array([[r, g, b]]) / 255.0  # Normalize
                rgb_input = scaler.transform(rgb_input)  # Scale

                # ทำนายผล
                prediction = svm_model.predict(rgb_input)
                predicted_season = label_encoder.inverse_transform(prediction)[0]

                st.write(f"The predicted season for RGB ({r}, {g}, {b}) is **{predicted_season}**.")

if __name__ == "__main__":
    main()