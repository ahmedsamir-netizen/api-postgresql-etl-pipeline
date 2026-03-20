from extract import extract_data
from transform import transform_data
from load import create_table, load_data


def run_pipeline():
    print("Starting ETL pipeline...")

    data, raw_file = extract_data()
    print(f"Extract step completed. Raw file: {raw_file}")

    df, processed_file = transform_data(data)
    print(f"Transform step completed. Processed file: {processed_file}")

    create_table()
    print("Table created successfully.")

    load_data(df)
    print(f"Load step completed. Inserted {len(df)} records.")

    print("ETL pipeline finished successfully.")

    print(f"loaded {len(df)} records into the PostgreSQL database.")

    print(df.head())

if __name__ == "__main__":
    run_pipeline()