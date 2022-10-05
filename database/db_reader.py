"""
This file provides *SAMPLE CODE* for reading from our DB for downstream tasks
"""
import os
import numpy as np
import psycopg2
from psycopg2 import sql

def insert_into_db(data_dir, conn):
    cursor = conn.cursor()
    q = sql.SQL("SELECT * from fashion_mnist")
    cursor.execute(q)
    for pair in cursor:
        label, image = pair
        image = np.frombuffer(image, dtype=np.float32).reshape((1, 28, 28))  # a single image
        print(image)

    cursor.close()
    conn.close()

if __name__ == '__main__':
    data_dir = "../data/sourced_data"
    conn = psycopg2.connect(
        host="localhost",
        database="fsdl",
        user="iq",
        password="ian"
    )
    insert_into_db(data_dir, conn)