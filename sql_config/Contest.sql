CREATE TABLE Contest (
    Id INT PRIMARY KEY,
    group_id INT,
    contest_name VARCHAR(64),
    Start_time DATETIME,
    Duration INT,
    Contest_level INT,
    FOREIGN KEY (group_id) REFERENCES groups(Id)
);
