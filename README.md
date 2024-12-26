# Personal Finance Tracker

## Overview

The Personal Finance Tracker is a Python-based application designed to help users efficiently manage their personal finances. This project demonstrates skills in Python programming, modular design, and file handling. It enables users to:

- Track and categorize income and expenses
- Save and retrieve financial transactions from a CSV file
- Filter and analyze financial data based on various criteria

This project showcases problem-solving abilities and attention to detail, making it a valuable addition to a software development or data analysis portfolio.

## Features

1. **Transaction Management**
   - Add and categorize transactions (income and expenses)
   - View all recorded transactions
   - Filter transactions by date, type, category, or amount

2. **Data Persistence**
   - Save transactions to a CSV file for long-term storage
   - Load transactions from a CSV file for review or modification

3. **Input Validation**
   - Ensures data accuracy for:
     - Dates (validated format)
     - Transaction types (income/expense)
     - Categories (customizable)
     - Monetary amounts (numeric validation)
     - Descriptions (text entries)

4. **Scalability**
   - Built with modular Python scripts to facilitate future expansions, such as:
     - AI/ML-based financial insights
     - Enhanced data visualization features

## Technical Skills Demonstrated

- **Programming Languages**: Python
- **Concepts and Techniques**: Modular programming, file I/O, data validation
- **Tools Used**: CSV handling, Python Standard Library

## File Structure

- `main.py`: The entry point of the application.
- `data_handler.py`: Module for reading and writing transaction data to/from CSV files.
- `Validators.py`: Module for user input validation to ensure consistent and reliable data.
- `transactions.csv`: Default file for storing transaction records.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Ryanlee34/personal-finance-tracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd personal-finance-tracker
   ```

3. Install required Python packages (if applicable):

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If no external libraries are used, skip this step.*

4. Run the application:

   ```bash
   python main.py
   ```

## Usage

1. Launch the application by running `main.py`.
2. Use the intuitive menu options to:
   - Add new transactions
   - View or filter existing transactions
   - Save data for future use
3. Review and analyze your financial data as needed.


## Future Enhancements

- AI/ML integration to offer budgeting advice and trend analysis.
- Graphical User Interface (GUI) for enhanced user experience.
- Exporting reports to Excel, PDF, or other formats.

## Contributing

Contributions are welcome! To propose changes or improvements:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m 'Add feature'
   ```

4. Push to the branch:

   ```bash
   git push origin feature-name
   ```

5. Open a pull request.

## Author

Developed by Kenneth Lee, a Computer Science student at Western Governors University. Passionate about software development and data analysis, with a focus on building efficient, scalable solutions. This project demonstrates foundational programming skills, modular design, and a commitment to practical learning and continuous improvement.







