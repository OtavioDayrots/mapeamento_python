# ARQUIVO USADO APENAS PARA CRIA SHAPEFILE SIMULADO
import shapefile

# Criar o shapefile (ESRI Shapefile)
shp = shapefile.Writer("bairros_simulados")
shp.field("nome", "C")
shp.field("codigo", "N")

# Lista de bairros simulados
bairros = [
    ("Centro", 1001, [[(0,0), (0,1), (1,1), (1,0), (0,0)]]),
    ("Bela Vista", 1002, [[(1,0), (1,1), (2,1), (2,0), (1,0)]]),
    ("São Francisco", 1003, [[(0,1), (0,2), (1,2), (1,1), (0,1)]]),
    ("Monte Castelo", 1004, [[(1,1), (1,2), (2,2), (2,1), (1,1)]]),
    ("Universitário", 1005, [[(2,0), (2,1), (3,1), (3,0), (2,0)]])
]

# Adiciona os bairros ao shapefile
for nome, codigo, poligono in bairros:
    shp.record(nome, codigo)
    shp.poly(poligono)

# Salvar os arquivos
shp.close()
print("Shapefile gerado com sucesso!")
