# Email/SMS Spam Classifier

This repository contains an Email/SMS Spam Classifier that predicts whether a given text is spam or not. The project employs a Random Forest Classifier (RFC) with hyperparameter tuning to achieve high precision and accuracy.

---

## 📖 Project Overview

### Objective
The goal of this project is to classify input text as spam or not spam using machine learning techniques. A strong focus has been placed on achieving high **precision**, ensuring the model minimizes false positives for spam detection.

### Key Features
- **Text Preprocessing**:
  - Tokenization
  - Removal of stop words, punctuation, and special characters
  - Stemming
- **Vectorization**: Text is transformed using the **TF-IDF (Term Frequency-Inverse Document Frequency)** method to create numerical feature vectors.
- **Model Selection**:
  - Several classification models were evaluated.
  - The **Random Forest Classifier** demonstrated the best performance in terms of **precision** and **accuracy**.
- **Deployment**: The model is deployed using **Streamlit Cloud**, providing an interactive web interface.

---

## 🚀 Live Demo
Access the deployed application here: [Spam Classifier on Streamlit](https://sandeshchh30-email-sms-spam-classifier-app-cg2m1a.streamlit.app/)

---

## 🛠️ Installation

Follow these steps to set up and run the project locally:

### Prerequisites
- Python 3.7 or later
- Required Python libraries (listed in `requirements.txt`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/sandeshchh30/Email-SMS-Spam-Classifier.git
   cd Email-SMS-Spam-Classifier
2. Install the dependencies:
   ```bash
    pip install -r requirements.txt
3. Run the application locally:
   ```bash
   streamlit run app.py

--- 

## 📝 Usage
- Open the application in your browser (usually at http://localhost:8501).
- Enter the text you want to classify in the input field.
- Click the Predict button to see whether the text is classified as spam or not.
