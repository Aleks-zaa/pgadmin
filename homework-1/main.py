"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="1122")
try:
    with conn:
        with conn.cursor() as cur:
            with open(f'north_data/employees_data.csv') as file:
                header = next(file)
                reader = csv.reader(file)
                for row in reader:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
            with open(f'north_data/customers_data.csv') as file:
                header = next(file)
                reader = csv.reader(file)
                for row in reader:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
            with open(f'north_data/orders_data.csv') as file:
                header = next(file)
                reader = csv.reader(file)
                for row in reader:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)
                # cur.execute("SELECT * FROM orders_data")
                # rows = cur.fetchall()
                # for row in rows:
                #     print(row)
finally:
    conn.close()
