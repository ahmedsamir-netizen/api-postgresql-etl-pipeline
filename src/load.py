from db import get_connection
import pandas as pd

def create_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        product_id INT PRIMARY KEY,
        title TEXT,
        description TEXT,
        category TEXT,
        price NUMERIC(10, 2),
        rating_rate NUMERIC(3, 2),
        stock INT,
        brand TEXT,
        image_url TEXT
    );
    """

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(create_table_query)
    conn.commit()
    cur.close()
    conn.close()


def load_data(df):
    insert_query = """
    INSERT INTO products (
        product_id, title, description, category, price,
        rating_rate, stock, brand, image_url
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (product_id) DO NOTHING;
    """

    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(insert_query, (
            int(row["product_id"]),
            row["title"],
            row["description"],
            row["category"],
            float(row["price"]) if pd.notna(row["price"]) else None,
            float(row["rating_rate"]) if pd.notna(row["rating_rate"]) else None,
            int(row["stock"]) if pd.notna(row["stock"]) else None,
            row["brand"],
            row["image_url"]
        ))

    conn.commit()
    cur.close()
    conn.close()