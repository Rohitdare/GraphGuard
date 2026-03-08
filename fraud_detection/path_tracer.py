from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "graphguard"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))


def trace_money_flow(account_id):

    query = """
    MATCH (a:Account {id:$account})-[t:TRANSFER*1..3]->(b)
    RETURN a,b
    LIMIT 50
    """

    with driver.session() as session:

        result = session.run(query, account=account_id)

        nodes = set()
        edges = []

        for record in result:

            a = record["a"]["id"]
            b = record["b"]["id"]

            nodes.add(a)
            nodes.add(b)

            edges.append({"source": a, "target": b})

        return {
            "nodes": list(nodes),
            "edges": edges
        }

if __name__ == "__main__":

    account = input("Enter account id: ")

    paths = trace_money_flow(account)

    print("Money Flow Paths Found:", len(paths))

    for p in paths:
        print(p)


def trace_incoming(account_id):

    query = """
    MATCH path=(a)-[:TRANSFER*1..5]->(b:Account {id:$account})
    RETURN path
    LIMIT 50
    """

    with driver.session() as session:

        result = session.run(query, account=account_id)

        paths = []

        for record in result:
            paths.append(record["path"])

        return paths
    

def get_account_network(account_id):

    query = """
    MATCH (a:Account {id:$account})-[t:TRANSFER]-(b)
    RETURN a,t,b
    LIMIT 50
    """

    with driver.session() as session:

        result = session.run(query, account=account_id)

        network = []

        for record in result:
            network.append(record)

        return network