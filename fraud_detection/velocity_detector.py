from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "graphguard"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))


def detect_velocity_fraud():

    query = """
    MATCH (a:Account)-[t:TRANSFER]->()
    WITH a, count(t) AS tx_count
    WHERE tx_count > 20
    RETURN a.id AS account, tx_count
    ORDER BY tx_count DESC
    """

    suspicious_accounts = []

    with driver.session() as session:

        result = session.run(query)

        for record in result:
            suspicious_accounts.append({
                "account": record["account"],
                "transactions": record["tx_count"]
            })

    return suspicious_accounts


if __name__ == "__main__":

    accounts = detect_velocity_fraud()

    print("Velocity Fraud Accounts")

    for acc in accounts:
        print(acc)