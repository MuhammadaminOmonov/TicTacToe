CREATE DATABASE IF NOT EXISTS TAOMLAR;
USE TAOMLAR;

CREATE TABLE IF NOT EXISTS taomlar(
    id INTEGER,
    taom_nomi TEXT,
    taom_masaliq TEXT
);

INSERT INTO taomlar (id, taom_nomi, taom_masaliq) VALUES
    (1, "Osh", "Kartoshka, Guruch, Go'sht"),
    (2, "Kabob", "Go'sht"),
    (3, "Somsa", "Un, Go'sht"),
    (4, "Shurva", "Kartoshka, Yog'"),
    (5, "Shirguruch", "Sut, Guruch"),
    (6, "Sutlosh", "Guruch, Sut"),
    (7, "Chuchvara", "Go'sht, Un"),
    (8, "Manti", "Kartoshka, Un"),
    (9, "Norin", "Un, Go'sht"),
    (10, "Beshbarmoq", "Go'sht, Un");

-- 1 --
SELECT * FROM taomlar WHERE taom_nomi LIKE "%a";

-- 2 --
SELECT * FROM taomlar WHERE taom_masaliq LIKE "Guruch%" OR taom_masaliq LIKE "%Guruch%" OR taom_masaliq LIKE "%Guruch";

DROP DATABASE IF EXISTS taomlar;

\! cls