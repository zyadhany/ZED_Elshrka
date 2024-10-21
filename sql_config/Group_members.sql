CREATE TABLE Group_members (
    group_id INT,
    handle VARCHAR(255),
    Privilege_level INT,
    FOREIGN KEY (group_id) REFERENCES groups(Id),
    FOREIGN KEY (handle) REFERENCES users(handle),
    PRIMARY KEY (group_id, handle)
);
