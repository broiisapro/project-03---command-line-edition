import os
import csv
import json
from datetime import datetime
from collections import defaultdict

class BudgetTracker:
    def __innit__ (self):
        #initialize the tracker with some default values
        self.transactions = []
        self.categories = ['Food', 'Rent', 'Entertainment', 'Utilities', 'Transportation', 'Miscellaneous']
        self.file_name = 'transactions.json'
        self.load_transactions()
    
    def load_transactions(self):
        """Load transaction data from the file if it exists."""
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                self.transactions = [Transaction(**item) for item in data]
        else:
            print("No previous transaction data found. Starting fresh.")
    