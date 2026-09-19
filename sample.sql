CREATE TABLE Supplier(
    SNO TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);

INSERT INTO Supplier(SNO, SNAME, STATUS, CITY) 
VALUES
('S1', 'Smith', '20', 'London'),
('S2', 'Jones', '10', 'Paris'),
('S3', 'Balke', '30', 'Paris'),
('S4', 'Clarke', '20', 'London'),
('S5', 'Adams', '20', 'Athens')

SELECT * FROM Supplier