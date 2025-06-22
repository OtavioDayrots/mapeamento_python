# 🗺️ Consulta Espacial com SQL Server + Python

Este projeto demonstra como automatizar uma **consulta espacial** usando **Python** e **SQL Server**, simulando uma tarefa comum em empresas que trabalham com **geoprocessamento**.

---

## 🔧 Tecnologias utilizadas

- Python 3
- SQL Server Express + SSMS
- PyODBC (conexão com banco de dados)
- Pandas (exportação para CSV)
- GeoPandas (leitura e conversão de shapefiles)
- Dados espaciais com tipo `geometry` (SQL Server)

---

## ⚙️ O que o projeto faz

✅ Conecta ao banco de dados SQL Server  
✅ Lê shapefile (.shp) com GeoPandas  
✅ Converte as geometrias para WKT e armazena no SQL Server  
✅ Permite ao usuário digitar coordenadas (X, Y)  
✅ Consulta quais bairros contêm esse ponto usando `STContains()`  
✅ Exibe os bairros encontrados no terminal  
✅ Exporta os resultados para um arquivo `resultado.csv`

---

## 📁 Estrutura do projeto

```
mapeamento_python/
├── automacao_sqlserver_geo/
│   ├── dados/
│   │   └── bairros/          # Contém os arquivos shapefile
│   ├── database/
│   │   ├── __init__.py
│   │   └── conecta_sqlserver.py  # Script de conexão com SQL Server
│   ├── consulta_espacial.py      # Faz a consulta espacial interativa
│   ├── cria_shapefile.py         # Cria shapefile de exemplo
│   ├── importacao_shapefile.py   # Importa shapefile para o banco
│   ├── resultado.csv             # Arquivo de resultado gerado
│   └── requirements.txt          # Dependências do projeto
├── SQL/
│   └── scripts.sql              # Scripts SQL do projeto
└── README.md
```

## ▶️ Como executar

1. Clone o projeto:

```bash
git clone https://github.com/OtavioDayrots/mapeamento_python.git
cd mapeamento_python
```

2. Instale a dependência:

```bash
pip install -r requirements.txt
```

3.  Execute a importação do shapefile:

```bash
python automacao_sqlserver_geo/importacao_shapefile.py
```

4. Execute a consulta espacial:

```bash
python automacao_sqlserver_geo/consulta_espacial.py
```

## 💡 Exemplo de uso

```bash
Informe o eixo X: 1.5
Informe o eixo Y: 0.5

Bairros encontrados que contêm o ponto (1.5, 0.5):
- Centro

Arquivo 'resultado.csv' gerado com sucesso!
```

## 🤝 Autor

Otávio Dayrots  
🔗 [GitHub](https://github.com/OtavioDayrots)  
📧 Em busca de oportunidade na área de desenvolvimento e geotecnologia