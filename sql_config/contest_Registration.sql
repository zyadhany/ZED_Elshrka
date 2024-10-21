CREATE TABLE contest_Registration (
    handle VARCHAR(255),
    contest_id INT,
    FOREIGN KEY (handle) REFERENCES users(handle),
    FOREIGN KEY (contest_id) REFERENCES Contest(Id),
    PRIMARY KEY (handle, contest_id)
);
