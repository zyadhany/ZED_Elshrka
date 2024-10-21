CREATE TABLE submissions (
    Id INT PRIMARY KEY,
    handle VARCHAR(255),
    problem_id INT,
    time_submitted DATETIME,
    compiler VARCHAR(255),
    Code VARCHAR(4096),
    execution_time INT,
    solution_size INT,
    Status VARCHAR(255),
    FOREIGN KEY (handle) REFERENCES users(handle),
    FOREIGN KEY (problem_id) REFERENCES Problems(Id)
);
