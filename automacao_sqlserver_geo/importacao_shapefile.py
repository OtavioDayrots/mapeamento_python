import geopandas as gpd
from database.conecta_sqlserver import conectar

try:
    # Ler shapefile
    gdf = gpd.read_file("automacao_sqlserver_geo/dados/bairros/bairros_simulados.shp")

    # Converter geometria para WKT e extrair colunas necessárias
    gdf['wkt'] = gdf.geometry.apply(lambda x: x.wkt)
    dados_para_inserir = gdf[['nome', 'codigo', 'wkt']]

    con = conectar()
    cursor = con.cursor()

    # Criar tabela (se não existir)
    cursor.execute("""
    IF OBJECT_ID('dbo.Bairros', 'U') IS NULL
    BEGIN
        CREATE TABLE dbo.Bairros (
            id INT IDENTITY(1,1) PRIMARY KEY,
            nome NVARCHAR(255),
            codigo INT,
            area geometry
        )
    END
    """)
    con.commit()

    # Inserir dados
    for index, row in dados_para_inserir.iterrows():
        nome = row['nome']
        codigo = int(row['codigo'])
        wkt = row['wkt']
        query = """
        INSERT INTO dbo.Bairros (nome, codigo, area)
        VALUES (?, ?, geometry::STGeomFromText(?, 0))
        """
        cursor.execute(query, nome, codigo, wkt)
        
    print("Importação concluída!")
    con.commit()
    
except Exception as e:
    print("Erro:", e)

finally:
    cursor.close()
    con.close()
