import psycopg2

def delete_data(name, number):
    
    command = """
    CALL dlt(%s, %s)
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute(command, (name, number))
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)