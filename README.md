# PhishingGuard AI

AI-powered phishing URL detection system built using Python and Streamlit that identifies malicious websites using machine learning techniques.

---

## Features

- Detects malicious and safe URLs
- Machine Learning based prediction system
- Interactive Streamlit web interface
- Fast and lightweight application
- User-friendly interface

---

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy

---

## Project Structure

```bash
PhishingGuard-AI/
│
├── app.py
├── predictor.py
├── feature_extractor.py
├── model.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/
│   └── phishing_dataset.csv
│
├── screenshots/
│   └── homepage.png
│
└── notebooks/
    └── model_training.ipynb
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/PhishingGuard-AI.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
streamlit run app.py
```

---

## How It Works

1. User enters a URL
2. Features are extracted from the URL
3. Machine learning model analyzes the URL
4. Prediction result is displayed as:
   - Safe URL
   - Malicious URL

---

## Future Improvements

- Real-time threat intelligence integration
- Browser extension support
- Deep learning based detection
- URL reputation scoring
- Enhanced UI/UX

---

## Author

Anshika

---

## License

This project is open-source and available under the MIT License.
