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
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (
                        row['employee_id'], row['first_name'], row['last_name'], row['title'], row['birth_date'], row['notes']))

        # Commit the changes to the database
        conn.commit()

        # Open the customers_data.csv file
        with open('customers_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)
            for row in csv_reader:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s)", (
                    row['customer_id'], row['company_name'], row['company_name']))

        # Commit the changes to the database
        conn.commit()

        # Open the orders_data.csv file
        with open('orders_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)
            for row in csv_reader:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)", (
                    row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city']))

        # Commit the changes to the database
        conn.commit()

# Close the database connection
conn.close()
