CREATE TABLE IF NOT EXISTS precos_staging (
    product_name VARCHAR(255),
    price NUMERIC(10,2),
    scraped_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dim_produto_preco (
    sk_produto SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    price NUMERIC(10,2),
    is_active BOOLEAN,
    valid_from TIMESTAMP,
    valid_to TIMESTAMP
)

