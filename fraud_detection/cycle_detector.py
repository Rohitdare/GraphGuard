from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "graphguard"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def detect_cycles():

    query = """
    MATCH path=(a:Account)-[:TRANSFER*3..5]->(a)
    RETURN path
    LIMIT 20
    """

    with driver.session() as session:
        result = session.run(query)

        cycles = []

        for record in result:
            cycles.append(record["path"])

        return cycles


if __name__ == "__main__":

    cycles = detect_cycles()

    print("Suspicious cycles detected:", len(cycles))