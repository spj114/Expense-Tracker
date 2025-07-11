# 📊 Expense Tracking System

A sleek, full-stack application designed to help you effortlessly track and analyze your personal expenses. Built with a powerful FastAPI backend and an intuitive Streamlit frontend.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.46-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ✨ Key Features & Previews

This application provides a seamless experience for managing your finances. Below is a walkthrough of its core features.

### 1. Add and Update Daily Expenses

The core of the application is the `Add/Update` tab. Here, you can select any date and log up to 10 expense entries for that day. The form intelligently pre-fills with existing data, making updates quick and easy.

<p align="center">
  <img src="./screenshots/01-add-update-tab.png" alt="Add/Update Tab" width="800">
</p>

The intuitive calendar makes date selection a breeze.

<p align="center">
  <img src="./screenshots/02-date-picker.png" alt="Date Picker" width="600">
</p>

### 2. Analyze Spending by Category

Curious where your money is going? The `Analytics By Category` tab provides a powerful breakdown. Select a start and end date to generate a dynamic bar chart and a detailed table showing total spending and percentage for each category.

<p align="center">
  <img src="./screenshots/03-category-analytics.png" alt="Category Analytics Tab" width="800">
</p>

Hover over the bars to see precise details or expand the chart for a larger view.

<p align="center">
  <img src="./screenshots/04-interactive-chart.png" alt="Interactive Chart Detail" width="600">
</p>
<p align="center">
  <img src="./screenshots/06-interactive-chart2.png" alt="Interactive Chart Detail" width="600">
</p>

### 3. Track Monthly Trends

To understand your long-term spending habits, the `Analytics By Month` tab aggregates all your expenses and displays the total for each month. This is perfect for spotting trends and planning your budget.

<p align="center">
  <img src="./screenshots/05-monthly-analytics.png" alt="Monthly Analytics Tab" width="800">
</p>

---

## 🛠️ Tech Stack

-   **Backend:** FastAPI, Uvicorn
-   **Frontend:** Streamlit
-   **Database:** MySQL
-   **Core Libraries:** Pandas, `mysql-connector-python`, Pydantic, Requests

---

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites
- Python 3.8+
- An active MySQL Server instance.

### 2. Clone the Repository
```bash
git clone https://github.com/spj114/Expense-Tracker.git
cd Expense-Tracker
```

### 3. Set Up a Virtual Environment
```bash
# Create the environment
python -m venv venv

# Activate it (macOS/Linux)
source venv/bin/activate

# Activate it (Windows)
.\venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure the Database
-   Connect to your MySQL server and create a new database.
    ```sql
    CREATE DATABASE expense_manager;
    ```
-   Use the new database and create the `expenses` table with this schema:
    ```sql
    CREATE TABLE expenses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        expense_date DATE NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        category VARCHAR(255) NOT NULL,
        notes TEXT
    );
    ```

### 6. Set Up Environment Variables
-   Create a copy of the example environment file:
    ```bash
    cp .env.example .env
    ```
-   Open the newly created `.env` file and add your database credentials.

---

## ▶️ How to Run

You need **two separate terminals** to run the frontend and backend servers.

#### Terminal 1: Start the Backend (FastAPI)
```bash
uvicorn server:app --reload
```

#### Terminal 2: Start the Frontend (Streamlit)
```bash
streamlit run app.py
```

The application will be available at:
- **Frontend (Streamlit):** http://localhost:8501
- **Backend API (FastAPI):** http://localhost:8000
