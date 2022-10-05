"""
This file is our processor that takes the sourced data (data collected/ data continually collected) and inserts them
    directly into our DB
"""
import os
import numpy as np
import psycopg2
from psycopg2 import sql

def insert_into_db(data_dir, conn):
    cursor = conn.cursor()
    q = sql.SQL("INSERT INTO fashion_mnist VALUES(%s, %s)")

    for pth in sorted(os.listdir(data_dir)):
        npzf = np.load(f"{data_dir}/{pth}")
        x, y = npzf['x'], npzf['y']

        for (sample, label) in zip(x, y):
            arr_sample = sample.tobytes()
            arr_label = label.tolist()
            cursor.execute(q, (arr_label, arr_sample,))

            conn.commit()
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