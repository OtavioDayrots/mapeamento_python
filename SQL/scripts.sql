CREATE TABLE Bairros (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome VARCHAR(100),
    area geometry
);

-- exemplo: polígono simples
INSERT INTO Bairros (nome, area)
VALUES (
    'Centro',
    geometry::STGeomFromText('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))', 0)
);
