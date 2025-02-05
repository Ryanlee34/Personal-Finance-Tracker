# Personal Finance Tracker

## Overview

The **Personal Finance Tracker** is an enhanced Python-based application designed to help users manage their personal finances efficiently. This version introduces **database integration** with PostgreSQL for better data management, replacing the previous file-based system.

### Key Features:
- Track **income and expenses** with categorized transactions.
- Store and retrieve transactions using **PostgreSQL** for persistent data storage.
- **View transactions** by type (Income/Expense) and category.
- **Validate user input** for accurate and structured financial records.

---

## Features

- **Transaction Management**: Add and categorize transactions (income/expenses), view all recorded transactions, and filter transactions by type.
- **Database Integration**: Transactions are securely stored in a **PostgreSQL database** for persistent data storage.
- **Input Validation**: Ensures accurate data entry, including **date validation, transaction types, categories, and amounts**.
- **Scalability**: Designed for future enhancements, including **AI/ML-based financial insights** and **automated budgeting recommendations**.

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
- **Ensure PostgreSQL is installed and running.**
- **Create a .env file in the project root and configure your database credentials**
```bash
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

```

## Future Enhancements

## Contributing
1. **Fork the repository** and create a new branch:
```bash
git checkout -b feature-name
git commit -m "Add feature"
git push origin feature-name
```


## Author
Developed by **Kenneth Lee**, a Computer Science student at Western Governors University, passionate about software development, data analysis, and AI/ML.









