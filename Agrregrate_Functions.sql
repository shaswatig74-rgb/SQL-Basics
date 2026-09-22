-- SQL AGRREGRATE FUNCTIONS
-- ACTIVITY: ZOO EXPLORER

-- ------- PART 1: Build and Explore the Table -------- --

CREATE TABLE IF NOT EXISTS zoo_animal (
    animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    age_years INTEGER NOT NULL,
    weight_kg REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO zoo_animal VALUES ('Lion', 'Big Cat', 5, 190.0);
INSERT INTO zoo_animal VALUES ('Tiger', 'Big Cat', 3, 220.0);
INSERT INTO zoo_animal VALUES ('Elephant', 'Pachyderm', 12, 4500.0);
INSERT INTO zoo_animal VALUES ('Giraffe', 'Ungulate', 7, 800.0);
INSERT INTO zoo_animal VALUES ('Penguin', 'Bird', 2, 5.0);
INSERT INTO zoo_animal VALUES ('Panda', 'Bear', 6, 95.0);
INSERT INTO zoo_animal VALUES ('Cheetah', 'Big Cat', 4, 55.0);
INSERT INTO zoo_animal VALUES ('Rhino', 'Pachyderm', 9, 2300.0);

SELECT * FROM zoo_animal;

-- -------- Part 2: SELECT DISTINCT -------- --

-- All species values including duplicates
SELECT species FROM zoo_animal;

-- Only unique species
SELECT DISTINCT(species) FROM zoo_animal;

-- Count how many unique species
SELECT COUNT(DISTINCT(species)) AS unique_species FROM zoo_animal;

-- --------- Part 3: COUNT -------- --
-- Total number of animals
SELECT COUNT(animal_id) AS total_animals FROM zoo_animal;

-- Animals older than 5 years
SELECT COUNT(animal_id) AS older_than_5 FROM zoo_animal WHERE age_years > 5;

-- -------- Part 4: SUM and AVG -------- --
 -- Total weight of all animals
SELECT SUM(weight_kg) AS total_weight_kg FROM zoo_animal;

-- Average age of all aniamls