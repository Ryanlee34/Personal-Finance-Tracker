class Transaction:
    """
    Represents a financial transaction with relevant attributes.
    """

    def __init__(self, date, transaction_type, category, income_type, amount, details):
        """Initialize a Transaction object with required attributes."""
        self.date = date
        self.transaction_type = transaction_type
        self.category = category
        self.income_type = income_type
        self.amount = amount
        self.details = details

    def __str__(self):
        """Return a string representation of the transaction."""
        return f"{self.date} | {self.transaction_type} | {self.category} | {self.income_type or 'N/A'} | ${self.amount} | {self.details}"
