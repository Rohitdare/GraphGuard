from neo4j import GraphDatabase

class Neo4jConnection:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]


if __name__ == "__main__":
    conn = Neo4jConnection("bolt://localhost:7687", "neo4j", "graphguard")

    result = conn.run_query("RETURN 'Connected to Neo4j' AS message")

    print(result)