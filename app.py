from neo4j import GraphDatabase as gd

uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"

driver = gd.driver(uri, auth=(user, password))

with driver.session() as session:
    result = session.run("MATCH (n) RETURN n LIMIT 10")
    for record in result:
        print(record)

    driver.close()
