from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j","graphguard"))

def detect_structuring():

    query = """
    MATCH (a:Account)-[t:TRANSFER]->()
    WHERE t.amount > 800000
    RETURN a.id, count(t) AS suspicious_tx
    ORDER BY suspicious_tx DESC
    LIMIT 10
    """

    with driver.session() as session:
        result = session.run(query)

        for record in result:
            print(record)


if __name__ == "__main__":
    detect_structuring()