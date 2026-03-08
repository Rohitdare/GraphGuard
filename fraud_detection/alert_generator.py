from neo4j import GraphDatabase
from risk_engine import calculate_risk

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "graphguard"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))


def create_alert(tx, account, score):

    query = """
    MATCH (a:Account {id:$account})

    CREATE (alert:Alert {
        account:$account,
        risk_score:$score,
        status:'OPEN'
    })

    CREATE (a)-[:FLAGGED]->(alert)
    """

    tx.run(query, account=account, score=score)


def generate_alerts():

    scores = calculate_risk()

    with driver.session() as session:

        for account, score in scores.items():

            if score > 70:

                session.execute_write(create_alert, account, score)


if __name__ == "__main__":

    generate_alerts()

    print("Fraud alerts generated")