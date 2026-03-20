import os
import pandas as pd
from datetime import datetime


def transform_data(data):
    df = pd.json_normalize(data)

    rename_map = {
        "id": "product_id",
        "category": "category",
        "description": "description",
        "price": "price",
        "rating": "rating_rate",
        "stock": "stock",
        "brand": "brand",
        "thumbnail": "image_url",
        "title": "title"
    }

    df = df.rename(columns=rename_map)

    selected_columns = [
        "product_id",
        "title",
        "description",
        "category",
        "price",
        "rating_rate",
        "stock",
        "brand",
        "image_url"
    ]

    df = df[selected_columns]

    df["product_id"] = pd.to_numeric(df["product_id"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["rating_rate"] = pd.to_numeric(df["rating_rate"], errors="coerce")
    df["stock"] = pd.to_numeric(df["stock"], errors="coerce")

    for col in ["title", "description", "category", "brand", "image_url"]:
        df[col] = df[col].astype(str).str.strip()

    os.makedirs("data/processed", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"data/processed/products_cleaned_{timestamp}.csv"

    df.to_csv(file_path, index=False)

    return df, file_path