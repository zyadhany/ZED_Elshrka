CREATE TABLE Friends (
    handle_one VARCHAR(255),
    handle_two VARCHAR(255),
    FOREIGN KEY (handle_one) REFERENCES users(handle),
    FOREIGN KEY (handle_two) REFERENCES users(handle),
    PRIMARY KEY (handle_one, handle_two)
);
