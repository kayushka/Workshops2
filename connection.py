from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def get_connection():
    cnx = connect(host='localhost', user='postgres',
                  database='warsztaty2', password='coderslab')
    cnx.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return cnx


