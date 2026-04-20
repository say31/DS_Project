# DS_Project
# 🌫️ Bangkok PM2.5 Forecasting & Anomaly Detection Dashboard

## 📌 Project Overview

This project presents an end-to-end **data science pipeline** for forecasting air pollution and detecting unusual pollution events in Bangkok.

The system combines:

* 📊 Historical air quality data
* 🌦️ Meteorological data
* 🤖 Machine learning models

to provide **insightful visualizations, predictions, and anomaly detection** through an interactive dashboard.

---

## 🎯 Objectives

* **Prediction**
  Forecast next-day PM2.5 levels using machine learning models.

* **Anomaly Detection**
  Identify abnormal pollution events beyond normal seasonal patterns.

* **Visualization**
  Provide an intuitive dashboard for non-technical users.

---

## 🌐 Live Dashboard

👉 *[Add your Streamlit link here]*

Example:
https://your-app-name.streamlit.app

---

## 📊 Features

* 📈 **PM2.5 Trends**

  * Interactive time-series visualization
  * Seasonal pollution patterns

* 🔮 **Prediction**

  * Next-day PM2.5 forecast
  * Clear interpretation (Good / Moderate / High pollution)

* ⚠️ **Anomaly Detection**

  * Isolation Forest model
  * Highlights unusual pollution events

* 📅 **Date Filtering**

  * Dynamic filtering via sidebar

---

## 🧠 Machine Learning Models

### Supervised Learning (Prediction)

* Random Forest Regressor
* Feature Engineering:

  * Lag features (t-1, t-7, etc.)
  * Rolling averages
  * Seasonal encoding

### Unsupervised Learning (Anomaly Detection)

* Isolation Forest
* Detects statistical outliers in pollution patterns

---

## 🗂️ Project Structure

```bash
pm25-dashboard/
│
├── app.py                  # Streamlit dashboard
├── final_dataset.csv       # Cleaned dataset with predictions & anomalies
├── requirements.txt       # Dependencies
├── notebook.ipynb         # Data processing & model training
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/say31/pm25-dashboard.git
cd pm25-dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 📦 Data Sources

* Open-Meteo API (Weather & Environmental Data)
* Local PM2.5 dataset (Bangkok air quality)

---

## 📈 Example Output

* Daily PM2.5 trends
* Next-day prediction with date
* Anomaly points highlighted in red

---

## 🚀 Deployment

The dashboard is deployed using **Streamlit Community Cloud**.

---

## 💡 Key Insights

* PM2.5 levels show strong seasonal patterns
* Wind speed and precipitation significantly affect pollution
* Anomalies often correspond to extreme environmental events

---

## 📄 License

This project is for academic and educational purposes.
