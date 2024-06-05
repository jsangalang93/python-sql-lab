import psycopg2
import psycopg2.extras
connection = psycopg2.connect(database='')

cursor = connection.cursor()

cursor.close()
connection.close()