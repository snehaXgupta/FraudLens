# AuthentiX — AI-Powered Fake Review Detection System

AuthentiX (also known as **FraudLens**) is an advanced machine learning and natural language processing (NLP) intelligence platform designed to identify fraudulent, computer-generated, and biased product reviews on major e-commerce platforms. 

The application features a sleek responsive dashboard with multiple input modalities, analytical charts, a diagnostic verification sequence pipeline, a sandbox presentation, and real-time sentiment correlation.

---

## ✨ Key Features

1. **Manual Text Scanner**: Direct verification of review content by analyzing token distributions and syntax flags.
2. **Product URL Crawler**: Real-time extraction and analysis of product reviews directly from active Amazon, Flipkart, or eBay product pages.
3. **Voice Scanner**: Integrated in-browser Web Speech API transcription allowing users to record review audio directly.
4. **Bulk CSV / Batch Scanner**: **[NEW]** High-throughput scanner that processes uploaded review spreadsheets, runs pipeline predictions in parallel, logs results, and outputs a downloadable annotated CSV report.
5. **Interactive Help Chatbot**: Support widget powered by simulated NLP context queries for troubleshooting and developer metrics.
6. **Built-in Presentation Deck**: Widescreen presentation slides ready to show coordinators, built natively inside `presentation.html`.

---

## 🛠️ Tech Stack & Libraries

* **Backend Framework**: Python (Flask) with session management and REST APIs.
* **WSGI Server**: Gunicorn (configured for production).
* **Machine Learning Pipeline**: Scikit-Learn (Logistic Regression, TF-IDF Vectorizer).
* **Natural Language Processing**: NLTK for stopword filtering, Regex for character cleaning.
* **Web Scraping**: BeautifulSoup4 for HTML tag extraction, Selenium WebDriver (optional fallback).
* **Frontend Design**: Vanilla HTML5/CSS3 (velvet dark glassmorphic styling), JavaScript (AJAX, chart rendering via Chart.js, HTML5 Web Speech recognition).

---

## 📂 Project Structure

```text
AuthentiX/
│
├── static/                   # Styling, images, and frontend scripts
│   ├── css/                  # CSS Stylesheets
│   ├── images/               # App Logos and branding graphics
│   └── js/                   # dashboard.js and main.js
│
├── templates/                # HTML layout structures
│   ├── dashboard.html        # Main platform dashboard
│   ├── login.html            # User login panel
│   └── register.html         # User sign-up panel
│
├── app.py                    # Flask server, route controllers, ML prediction pipeline
├── fake_review_model.pkl     # Pickled Logistic Regression ML model weights
├── tfidf_vectorizer.pkl      # Pickled TF-IDF Vectorizer
├── generate_ppt.py           # Presentation slides compiler script
├── presentation.html         # Interactive web presentation slides
├── requirements.txt          # Python library dependencies (Render compatible)
├── Procfile                  # Process definition file for Render web services
├── test_reviews.csv          # Sample review file for verifying the Batch Scanner
└── README.md                 # System overview and deployment instructions
```

---

## 🚀 Setup & Local Execution

### 1. Prerequisite
Ensure you have Python installed (Python 3.9 - 3.13 recommended).

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/authentix.git
cd authentix
```

### 3. Create a Virtual Environment
```bash
python -m venv venv
# On Windows (cmd/PowerShell):
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Server
```bash
python app.py
```
Open [http://localhost:5000](http://localhost:5000) in your web browser.

---

## ☁️ Render Deployment Guide

AuthentiX is pre-configured and 100% ready to deploy to **Render**:

1. Create a new account or log in to [Render](https://render.com).
2. Connect your Git repository.
3. Choose **New > Web Service**.
4. Set the configurations:
   * **Runtime**: `Python`
   * **Build Command**: `pip install -r requirements.txt`
   * **Start Command**: `gunicorn app:app`
5. Click **Deploy**. Render will automatically read the `Procfile` and launch the app securely.

---

## 👥 Project Team & Credits

AuthentiX (FraudLens) is developed and maintained by:
* **Shaurya Bajpai** — *Lead Administrator*
* **Sneha Gupta** — *Database & Machine Learning Administrator*
* **Ritik Chaudhary** — *Security Administrator*
* **Ritika Singh** — *Systems Analyst Administrator*
