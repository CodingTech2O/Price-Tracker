# 🛒 Price Tracker

A lightweight Flask web application for tracking product prices.

Price Tracker lets you add products, monitor their prices, and manage price tracking through a simple web interface.

## ✨ Features

* 🛒 Track product prices
* 🌐 Web-based interface
* 🐍 Built with Python and Flask
* 🎨 HTML & CSS frontend
* 📝 Form-based product management
* ⚡ Lightweight and easy to run locally
* 📦 Dependency management with `uv`
* 🔒 Environment-variable based configuration

## 🛠️ Tech Stack

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS

### Tooling

* `uv`
* `pyproject.toml`

## 📁 Project Structure

```text
Price-Tracker/
│
├── static/
│   └── CSS and other static assets
│
├── templates/
│   └── HTML templates
│
├── app.py
├── forms.py
├── price_tracker.py
│
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Make sure you have:

* Python installed
* `uv` installed

You can verify your installation with:

```bash
python --version
uv --version
```

### 1. Clone the Repository

```bash
git clone https://github.com/CodingTech2O/Price-Tracker.git
cd Price-Tracker
```

### 2. Install Dependencies

Sync the project environment using `uv`:

```bash
uv sync
```

`uv` will create the virtual environment and install the dependencies defined in `pyproject.toml`.

### 3. Configure Environment Variables

Create a `.env` file in the project root and add the required environment variables.

```text
Price-Tracker/
├── .env
├── app.py
├── price_tracker.py
└── ...
```

> `.env` is ignored by Git and should never be committed to the repository.

### 4. Run the Application

```bash
uv run python app.py
```

Open the local address displayed by Flask in your browser.

## 🧠 How It Works

The application follows a simple Flask-based architecture:

```text
User
  │
  ▼
HTML/CSS Interface
  │
  ▼
Flask Routes
  │
  ├── Forms
  │
  └── Price Tracking Logic
          │
          ▼
      Product Data
```

The Flask application handles requests and routes while the price-tracking logic is separated into `price_tracker.py`.

## 📌 Project Goals

This project was built to explore and practice:

* Web development with Flask
* HTML form handling
* Web scraping and price extraction
* Python application structure
* Separating application logic from routes
* Dependency management with `uv`
* Building a practical automation-oriented web application


## ⚠️ Disclaimer

Prices and product availability can change at any time.

Always verify the final price and product details on the retailer's website before making a purchase.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Open a pull request

