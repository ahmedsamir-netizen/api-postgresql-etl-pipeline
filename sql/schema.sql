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