import pandas as pd
from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "graphguard"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))


def create_transaction(tx, row):

    query = """
    MERGE (a:Account {id:$sender})
    MERGE (b:Account {id:$receiver})
    CREATE (a)-[:TRANSFER {
        transaction_id:$transaction_id,
        amount:$amount,
        channel:$channel,
        timestamp:$timestamp,
        branch:$branch,
        is_fraud:$is_fraud
    }]->(b)
    """

    tx.run(query,
        transaction_id=row["transaction_id"],
        sender=row["sender"],
        receiver=row["receiver"],
        amount=int(row["amount"]),
        channel=row["channel"],
        timestamp=str(row["timestamp"]),
        branch=row["branch"],
        is_fraud=int(row["is_fraud"])
    )


def load_transactions():

    df = pd.read_csv("datasets/transactions.csv")

    print(f"Loading {len(df)} transactions into Neo4j...")

    with driver.session() as session:

        for _, row in df.iterrows():
            session.execute_write(create_transaction, row)

    print("Transactions loaded successfully.")


if __name__ == "__main__":
    load_transactions()