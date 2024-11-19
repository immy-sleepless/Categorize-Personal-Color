# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hRuzkSICyJ3tq7mpgBfChgSjLH6yTS0b
"""

!pip install streamlit

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# ฟังก์ชันสำหรับการโหลดและประมวลผลข้อมูล
@st.cache
def load_data(file):
    df = pd.read_csv(file)
    return df

# ฟังก์ชันสำหรับการสร้างโมเดล SVM
def train_svm_model(df):
    X = df[['R', 'G', 'B']]   # Features
    y = df['season']          # Labels

    # แปลง Labels (season) เป็นตัวเลข
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    # ปรับขนาดข้อมูล
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # สร้างโมเดล SVM
    svm_model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
    svm_model.fit(X_train, y_train)

    # ประเมินผลโมเดล
    y_pred = svm_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    return accuracy, conf_matrix, label_encoder.classes_

# ส่วน UI หลักของ Streamlit
def main():
    st.title("Personal Color Classification")
    st.write("Upload your color dataset and train an SVM model for classification.")

    # อัปโหลดไฟล์
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        # โหลดข้อมูล
        df = load_data(uploaded_file)
        st.write("Dataset Preview:")
        st.dataframe(df.head())

        if st.button("Train Model"):
            st.write("Training the SVM model...")
            accuracy, conf_matrix, class_labels = train_svm_model(df)

            st.write(f"Model Accuracy: {accuracy:.2f}")

            # แสดง Confusion Matrix
            st.write("Confusion Matrix:")
            fig, ax = plt.subplots()
            sns.heatmap(conf_matrix, annot=True, cmap='Blues', xticklabels=class_labels, yticklabels=class_labels, ax=ax)
            plt.xlabel("Predicted")
            plt.ylabel("Actual")
            plt.title("Confusion Matrix")
            st.pyplot(fig)

if __name__ == "__main__":
    main()