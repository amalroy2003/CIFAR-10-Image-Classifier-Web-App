# 🚀 CIFAR‑10 Image Classifier Web App

A lightweight **Streamlit** web app that classifies uploaded images into one of the ten **CIFAR‑10** categories using a pre‑trained **TensorFlow/Keras CNN**.

> Upload a 32 × 32 image (e.g., a dog, ship, airplane, etc.) and the model will predict the class and its confidence.

---

## 🧠 CIFAR‑10 Classes

| Index | Emoji | Class      |
|------:|:-----:|------------|
| 0     | ✈️     | **Airplane**   |
| 1     | 🚗     | **Automobile** |
| 2     | 🐦     | **Bird**       |
| 3     | 🐱     | **Cat**        |
| 4     | 🦌     | **Deer**       |
| 5     | 🐶     | **Dog**        |
| 6     | 🐸     | **Frog**       |
| 7     | 🐴     | **Horse**      |
| 8     | 🚢     | **Ship**       |
| 9     | 🚚     | **Truck**      |

---

## 📂 Project Layout

cifar10-streamlit-app/
├── image_classifier.py # Streamlit application
├── cifar10_model.h5 # Pre‑trained CNN model
├── requirements.txt # Python dependencies
└── README.md # (this file)


---

## ⚡ Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/amalroy2003/CIFAR-10-Image-Classifier-Web-App.git
cd cifar10-streamlit-app
