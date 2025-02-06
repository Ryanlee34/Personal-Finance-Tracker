# Personal Finance Tracker

## Overview

The **Personal Finance Tracker** is a Python-based application designed to help users manage their personal finances efficiently. This version integrates **PostgreSQL** for robust and persistent data storage and offers **data visualization** features for financial insights.

### **Key Features:**
- **Track Income and Expenses**: Add, categorize, and retrieve transactions (Income/Expense).
- **Database Integration**: Securely stores transactions using **PostgreSQL**.
- **Data Visualization**: Generates **pie charts** for income and expense distribution and a **line chart** for income vs. expenses over time.
- **View Transactions by Type**: Filter transactions based on **Income** or **Expense**.
- **Input Validation**: Ensures structured data entry, including **date validation, transaction types, categories, and amounts**.

---

## Features

### **1. Transaction Management**
- Add new transactions with **validated inputs**.
- Categorize transactions based on predefined **income sources** and **expense categories**.
- View all recorded transactions.
- Filter transactions based on **Income** or **Expense**.

### **2. Database Integration**
- Uses **PostgreSQL** for persistent and structured data storage.
- Stores transaction details, including **date, type, category, amount, and description**.
- Fetches transactions efficiently using **SQLAlchemy**.

### **3. Data Visualization**
- **Pie Chart**: Displays **income** and **expense** distributions.
- **Line Chart**: Tracks **income vs. expenses** over time.
- Uses **Matplotlib and Pandas** for visualization.

### **4. Input Validation**
- Ensures accurate and structured data entry:
  - **Date Validation** (YYYY-MM-DD format).
  - **Transaction Type Selection** (Income/Expense).
  - **Predefined Categories** for expenses and income types.
  - **Amount Validation** (Positive numeric values).

---

## **Installation & Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/YourUsername/personal-finance-tracker.git
cd personal-finance-tracker
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```
### **3. Set up PostgreSQL Database**
- **pip install -r requirements.txt**
- **Create a .env file in the project root and configure your database credentials:**
```bash
DB_NAME=finance_tracker
DB_USER=postgres
DB_PASSWORD=project1
DB_HOST=localhost
DB_PORT=5432
```
### **4. Run the Application**
```bash
python main.py
```

## **Usage Guide**

### **1. Add a New Transaction:**
- **Follow prompts to enter date, type (Income/Expense), category, amount, and description.**

### **2. View Transactions:**
- **View all transactions.**
- **Filter transactions by Income or Expense.**

### **3. Generate Financial Reports:**
- **Pie Chart for Income Distribution.**
- **Pie Chart for Expense Distribution.**
- **Line Chart for Income vs. Expenses over time.**

## **Future Enhancements**
- **AI/ML-based financial insights.**
- **Automated budgeting recommendations.**
- **Multi-user support with authentication.**
- **Export transactions to CSV/Excel.**
- **Mobile-friendly UI using Flask/Django.**

## **Author**
Developed by **Kenneth Lee**, a Computer Science student at Western Governors University, passionate about software development, data analysis, and AI/ML.
