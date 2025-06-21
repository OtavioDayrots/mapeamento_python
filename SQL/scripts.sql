CREATE TABLE Bairros (
        id INT IDENTITY(1,1) PRIMARY KEY,
        nome NVARCHAR(255),
        codigo INT,
        area geometry
    )

-- exemplo: polígono simples
INSERT INTO Bairros (nome, codigo, area)
VALUES (
    'Centro',
    123,
    geometry::STGeomFromText('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))', 0)
);
