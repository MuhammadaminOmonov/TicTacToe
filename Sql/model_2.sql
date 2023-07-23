CREATE DATABASE IF NOT EXISTS UNIVERSITET;
USE UNIVERSITET;

CREATE TABLE IF NOT EXISTS talabalar(
    id INTEGER,
    talaba_ism TEXT,
    talaba_kurs INTEGER,
    talaba_stipendiya INTEGER
);

INSERT INTO talabalar (id, talaba_ism, talaba_kurs, talaba_stipendiya) VALUES
    (1, "Saloh", 2, 100000),
    (2, "Malik", 3, 120000),
    (3, "Qodir", 4, 80000),
    (4, "Salom", 1, 70000),
    (5, "Komil", 2, 80000),
    (6, "Vali", 4, 180000),
    (7, "Akbar", 3, 150000),
    (8, "Aziz", 4, 160000),
    (9, "Islom", 2, 130000),
    (10, "Hakim", 1, 110000);

-- 1 --
DELETE FROM talabalar WHERE talaba_kurs = 4;

UPDATE talabalar SET talaba_kurs = talaba_kurs + 1 WHERE talaba_kurs < 4;

-- 2 --
SELECT count(talaba_kurs = 1) FROM talabalar  WHERE talaba_kurs = 1; 
SELECT count(talaba_kurs = 2) FROM talabalar  WHERE talaba_kurs = 2; 
SELECT count(talaba_kurs = 3) FROM talabalar  WHERE talaba_kurs = 3; 
SELECT count(talaba_kurs = 4) FROM talabalar  WHERE talaba_kurs = 4;

DROP DATABASE IF EXISTS talabalar;

\! cls
