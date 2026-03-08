import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker()

NUM_ACCOUNTS = 1000
NUM_TRANSACTIONS = 20000

channels = ["UPI", "NEFT", "RTGS", "IMPS", "CASH"]

accounts = [f"A{i}" for i in range(1, NUM_ACCOUNTS + 1)]

transactions = []

for i in range(NUM_TRANSACTIONS):

    sender = random.choice(accounts)
    receiver = random.choice(accounts)

    while receiver == sender:
        receiver = random.choice(accounts)

    amount = random.randint(500, 500000)

    channel = random.choice(channels)

    timestamp = fake.date_time_this_year()

    branch = f"BR{random.randint(1,20)}"

    transaction_id = f"TX{i+1:06d}"

    transactions.append({
        "transaction_id": transaction_id,
        "sender": sender,
        "receiver": receiver,
        "amount": amount,
        "channel": channel,
        "timestamp": timestamp,
        "branch": branch,
        "is_fraud": 0
    })

df = pd.DataFrame(transactions)

df.to_csv("datasets/transactions.csv", index=False)

print("Transaction dataset generated successfully")