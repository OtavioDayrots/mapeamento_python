from database.conecta_sqlserver import conectar
import pandas as pd

# Consulta espacial
def buscarBairros(x, y, cursor):
    ponto = f"geometry::STGeomFromText('POINT({x} {y})', 0)"
    query = f"""
        DECLARE @ponto geometry = {ponto};
        SELECT nome FROM Bairros WHERE area.STContains(@ponto) = 1;
    """
    cursor.execute(query)
    return [row.nome for row in cursor.fetchall()]

try:
    con = conectar()
    cursor = con.cursor()
    
    while True:
        try:
            eixoX = float(input("Informe o eixo X: "))
            eixoY = float(input("Informe o eixo Y: "))
            break
            
        except ValueError:
            print("Por favor, digite valores numéricos.")
            continue
        
    # Coletar resultados
    nomes = buscarBairros(eixoX, eixoY, cursor)
    
    if nomes:
        # Exibir no terminal
        print(f"Bairros encontrados que contêm o ponto ({eixoX}, {eixoY}):")
        for nome in nomes:
            print("-", nome)

        # Exportar para CSV
        df = pd.DataFrame(nomes, columns=["Bairro"])
        df.to_csv("automacao_sqlserver_geo/resultado.csv", index=False, encoding="utf-8")

        print("\nArquivo 'resultado.csv' gerado com sucesso!")
        
    else:
        print("Nenhum bairro encontrado para esse ponto.") 

except Exception as e:
    print("Erro:", e)

finally:
    cursor.close()
    con.close()
