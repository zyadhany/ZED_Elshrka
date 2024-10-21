CREATE TABLE Problems (
    Id INT PRIMARY KEY,
    Rate INT,
    Name VARCHAR(64),
    contest_id INT,
    FOREIGN KEY (contest_id) REFERENCES Contest(Id)
);
