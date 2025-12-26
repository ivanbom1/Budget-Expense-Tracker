CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);


CREATE TABLE pockets (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    pocket_name VARCHAR(255) NOT NULL,
    description TEXT,
    balance DECIMAL(10, 2) DEFAULT 0,
    goal DECIMAL(10, 2),
    currency VARCHAR(3)
);

