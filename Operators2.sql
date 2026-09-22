-- SELECT * FROM zoo_animal;

-- -- AND
-- SELECT name, species, age_years FROM zoo_animal WHERE weight_kg >= 100.0 AND age_years >= 2;

-- -- OR
-- SELECT * FROM zoo_animal WHERE age_years >= 15 OR weight_kg > 4000;

-- -- LIKE
-- SELECT * FROM zoo_animal WHERE name LIKE '%gui%';

-- -- MIN
-- SELECT * FROM zoo_animal WHERE age_years = (SELECT MIN(age_years) FROM zoo_animal);

-- -- MAX
-- SELECT * FROM zoo_animal WHERE weight_kg = (SELECT MAX(weight_kg) FROM zoo_animal);

-- -- UPDATE
-- UPDATE zoo_animal SET weight_kg = 180.0 WHERE name = 'Lion';

-- INSERT INTO zoo_animal(name, species, age_years, weight_kg) VALUES ('Parrot', 'Bird', 1, 2.0);

-- -- DELETE 
-- DELETE FROM zoo_animal WHERE name = 'Parrot';

-- -- CRUD - Create, Read, Update, Delete