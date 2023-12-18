from flask import Flask, request, jsonify
import os
import mysql.connector

app = Flask(__name__)

def connect_to_mysql():
    # Get the database connection details from environment variables
    db_host = os.getenv('DB_HOST') or 'mysql-container'  # Replace 'mysql-container' with the actual container name
    db_user = os.getenv('DB_USER') or 'root'  # Replace 'root' with the actual database user
    db_password = os.getenv('DB_PASSWORD') or 'password'  # Replace 'password' with the actual database password
    db_name = os.getenv('DB_NAME') or 'your_database'  # Replace 'your_database' with the actual database name

    print("Connecting to the database with URL:", db_host)

    try:
        print(f"Connecting to the database at {db_host}...")
        return mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        raise  # Propagate the exception

def create_appointment_table(table_name, connection):
    cursor = connection.cursor()
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            doctor_username VARCHAR(255),
            patient_username VARCHAR(255),
            day_of_week VARCHAR(255),
            time_slot VARCHAR(255)
        )
    """
    cursor.execute(create_table_query)
    connection.commit()

# ... (Rest of your code)

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    # Connect to the MySQL database
    db_connection = connect_to_mysql()

    # Create the appointment table if it does not exist
    create_appointment_table('appointments', db_connection)

    # Run the Flask app
    app.run(port=port, host='0.0.0.0')
