# 🗺️ Consulta Espacial com SQL Server + Python

Este projeto demonstra como automatizar uma **consulta espacial** usando **Python** e **SQL Server**, simulando uma tarefa comum em empresas que trabalham com **geoprocessamento**.

---

## 🔧 Tecnologias utilizadas

- Python 3
- SQL Server Express + SSMS
- PyODBC (conexão)
- Pandas (exportação de resultados)
- Dados espaciais com tipo `geometry`

---

## ⚙️ O que o script faz

✅ Conecta ao banco de dados SQL Server  
✅ Cria um ponto espacial com `STGeomFromText`  
✅ Consulta quais bairros (polígonos) contêm esse ponto usando `STContains`  
✅ Exibe os bairros encontrados no terminal  
✅ Exporta os dados encontrados para um arquivo `resultado.csv`

---

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

3. Execute o script:

```bash
python consulta_bairros.py
```