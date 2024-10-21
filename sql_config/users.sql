CREATE TABLE users (
    account_id INT,
    handle VARCHAR(64) PRIMARY KEY,
    Gender VARCHAR(64),
    Date_of_birth DATE,
    rate INT,
    Image BLOB,
    status VARCHAR(255),
    FOREIGN KEY (account_id) REFERENCES accounts(Id)
);
