import psycopg2
import csv

# Connect to the PostgreSQL database
with psycopg2.connect(host='localhost', database='north', user='postgres', password='Lunkaç§') as conn:
    with conn.cursor() as cur:

        # Open the employees_data.csv file
        with open('employees_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)
            for row in csv_reader:
                cur.execute('INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)',
                               (row[0], row[1], row[2], row[3], row[4], row[5]))

        # Commit the changes to the database
        conn.commit()

        # Open the customers_data.csv file
        with open('customers_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)
            for row in csv_reader:
                cur.execute('INSERT INTO customers VALUES(%s, %s, %s)',
                            (row[0], row[1], row[2]))

        # Commit the changes to the database
        conn.commit()

        # Open the orders_data.csv file
        with open('orders_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)
            for row in csv_reader:
                cur.execute('INSERT INTO orders VALUES(%s, %s, %s, %s, %s)',
                            (row[0], row[1], row[2], row[3], row[4]))

        # Commit the changes to the database
        conn.commit()

# Close the database connection
conn.close()
