import os
import json
import requests
from datetime import datetime

API_URL = "https://dummyjson.com/products"


def extract_data():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()

    payload = response.json()
    data = payload["products"]

    os.makedirs("data/raw", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"data/raw/products_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    return data, file_path


if __name__ == "__main__":
    data, file_path = extract_data()
    print(f"Extracted {len(data)} records")
    print(f"Saved raw data to: {file_path}")