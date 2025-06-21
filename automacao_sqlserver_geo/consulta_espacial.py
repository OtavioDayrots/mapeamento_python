from database.conecta_sqlserver import conectar
import pandas as pd

try:
    con = conectar()
    cursor = con.cursor()

    # Consulta espacial
    ponto = "geometry::STGeomFromText('POINT(0.5 0.5)', 0)"
    query = f"""
        DECLARE @ponto geometry = {ponto};
        SELECT nome FROM Bairros WHERE area.STContains(@ponto) = 1;
    """

    cursor.execute(query)

    # Coletar resultados
    nomes = [row.nome for row in cursor.fetchall()]

    # Exibir no terminal
    print("Bairros encontrados que contêm o ponto (0.5, 0.5):")
    for nome in nomes:
        print("-", nome)

    # Exportar para CSV
    df = pd.DataFrame(nomes, columns=["Bairro"])
    df.to_csv("automacao_sqlserver_geo/resultado.csv", index=False, encoding="utf-8")

    print("\nArquivo 'resultado.csv' gerado com sucesso!")

except Exception as e:
    print("Erro:", e)

finally:
    cursor.close()
    con.close()

