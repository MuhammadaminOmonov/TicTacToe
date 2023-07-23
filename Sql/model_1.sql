CREATE DATABASE IF NOT EXISTS computers;
USE computers;

CREATE TABLE IF NOT EXISTS computers(
    brand TEXT,
    model TEXT,
    cpu INTEGER,
    frequency FLOAT,
    ram INTEGER,
    os TEXT,
    price INTEGER
);

INSERT INTO computers(brand, model, cpu, frequency, ram, os, price) VALUES
    ("Apple", "Macbook 13", 8, 3.5, 16, "Macintosh 10", 1500),
    ("Asus", "ZenBook X5", 10, 4.2, 16, "Windows 10 Pro", 1200),
    ("Lenova", "Legion M2", 10, 5.2, 32, "Windows 11 Pro", 1700),
    ("Acer", "Acer 5 Pro", 6, 3.4, 8, "Windows 10", 800),
    ("Lenova", "Legion M1 Pro", 6, 5.2, 32, "Windows 11", 1300),
    ("Asus", "Asus 5 Pro", 4, 4.2, 8, "Windows 10", 900),
    ("Apple", "Macbook 14", 12, 4.5, 32, "Macintosh 12", 2500),
    ("Apple", "Macbook 13 Pro", 12, 4.5, 16, "Macintosh 11", 1800),
    ("Asus", "ZenBook X5", 10, 4.2, 16, "Windows 10 Pro", 1200),
    ("Lenova", "Legion M2", 10, 5.2, 32, "Windows 11 Pro", 1700),
    ("Acer", "Acer 5 Pro", 6, 3.4, 8, "Windows 10", 800),
    ("Lenova", "Legion M1 Pro", 6, 5.2, 32, "Windows 11", 1300),
    ("Asus", "Asus 5 Pro", 4, 4.2, 8, "Windows 10", 900),
    ("Apple", "Macbook 14", 12, 4.5, 32, "Macintosh 12", 2500),
    ("Apple", "Macbook 13", 8, 3.5, 16, "Macintosh 10", 1500),
    ("Asus", "ZenBook X5", 10, 4.2, 16, "Windows 10 Pro", 1200),
    ("Lenova", "Legion M2", 10, 5.2, 32, "Windows 11 Pro", 1700),
    ("Acer", "Acer 5 Pro", 6, 3.4, 8, "Windows 10", 800),
    ("Lenova", "Legion M1 Pro", 6, 5.2, 32, "Windows 11", 1300),
    ("Asus", "Asus 5 Pro", 4, 4.2, 8, "Windows 10", 900);

-- 1 --
SELECT price FROM computers ORDER BY price DESC LIMIT 1;
-- 2 --
SELECT price FROM computers ORDER BY price ASC LIMIT 1;
-- 3 --
SELECT frequency FROM computers WHERE price >= 400 AND price <= 1000 AND cpu <= 8;
-- 4 --
SELECT count(brand) FROM computers  WHERE brand = "Apple"; 
-- 5 --
SELECT price FROM computers WHERE os LIKE "Windows%" AND ram = 8 AND brand = "Asus";

DROP DATABASE IF EXISTS computer;

\! cls