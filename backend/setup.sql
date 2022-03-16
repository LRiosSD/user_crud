CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
)
CREATE TABLE vehicle(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(45) NOT NULL,
    license_plate VARCHAR (7) NOT NULL,
    v_type INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY(v_type) REFERENCES vehicle_type(id),
    FOREIGN KEY(user_id) REFERENCES usesr(id)
);

INSERT INTO vehicle(
    color,
    license_plate,
    v_type,
    user_id,
) VALUES(
    "blue",
    "ABC123",
    "sedan",
    "Leo"
)

INSERT INTO user(
    first_name,
    last_name,
    hobbies
) VALUES (
    "Lenardo",
    "Rios",
    "Learning"
)
INSERT INTO user(
    first_name,
    last_name,
    hobbies
) VALUES (
    "John",
    "Doe",
    "Biking"
)
INSERT INTO user(
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jane",
    "Doe",
    "Reading"
)