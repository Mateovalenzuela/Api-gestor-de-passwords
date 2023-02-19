import psycopg2
from psycopg2 import DatabaseError



def get_connection():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            database = "test_gestor_de_passwords",
            user = "postgres",
            password = "admin123")

        return conn
    except DatabaseError as ex:
        raise ex
