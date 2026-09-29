CREATE TABLE Neighbourhood(
    midtown TEXT PRIMARY KEY,
    downtown TEXT,
    chinatown TEXT,
    distance REAL
);

INSERT INTO Neighbourhood(midtown, downtown, chinatown, distance) VALUES
('Doha', 'Souq Waqif', 'Xian', 3.5 ),
('Al Khor', 'Musherib', 'Gwangzhou', 12);




CREATE TABLE Restaurants(
    name TEXT
    review REAL PRIMARY KEY,
    cuisine TEXT,
    rate TEXT,
    health_grade REAL
);

INSERT INTO Restaurants(name,review, cuisine, rate, health_grade) VALUES
('Huda',3.5, 'Lebanese', '$$$$$', NULL),
('Ashas',4.5, 'Indian', '$$$$', 4),
('PF Chang',4.3, 'Chinese', '$$$$$', NULL),
(' Papa Johns',4.8, 'Italian' '$$$', 4.6),
('Candy Crush',5, 'Italian', '$$', 3);

SELECT * FROM Restaurants WHERE cuisine = 'Chinese';
SELECT review FROM Restaurants WHERE  review >= 4;

SELECT * FROM Restaurants WHERE cuisine = 'Italian' and rate = '$$$';

SELECT name FROM Restaurants WHERE name = LIKE 'Candy%';

SELECT * FROM Neighbourhood WHERE distance = (SELECT MIN(distance) FROM Neighbourhood);

SELECT * FROM Restaurants WHERE health_grade IS NULL;

SELECT * FROM Restaurants WHERE review ORDER BY ASC LIMIT 4;
