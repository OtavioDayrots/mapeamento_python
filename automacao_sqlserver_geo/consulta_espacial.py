import pyodbc

# Conectar ao SQL Server
conexao = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'
    'DATABASE=Geoprocessamento;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'
)

cursor = conexao.cursor()

# Consulta espacial: verificar se o ponto está dentro de algum bairro
ponto = "geometry::STGeomFromText('POINT(0.5 0.5)', 0)"
query = f"""
    DECLARE @ponto geometry = {ponto};
    SELECT nome FROM Bairros WHERE area.STContains(@ponto) = 1;
"""

cursor.execute(query)

print("Bairros encontrados que contêm o ponto (0.5, 0.5):")
for row in cursor.fetchall():
    print("-", row.nome)

cursor.close()
conexao.close()
