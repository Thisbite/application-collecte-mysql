from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Utiliser les variables d'environnement
host = os.getenv('MYSQL_HOST')
database = os.getenv('MYSQL_DATABASE')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')

# Exemple d'utilisation pour créer une connexion
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        conn = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if conn.is_connected():
            print("Connexion à la base de données MySQL réussie")
            return conn
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL : {e}")
        return None
create_connection()