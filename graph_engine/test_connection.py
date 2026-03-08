from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j","graphguard"))

with driver.session() as session:
    result = session.run("RETURN 'Connected' AS message")
    print(result.single()["message"])